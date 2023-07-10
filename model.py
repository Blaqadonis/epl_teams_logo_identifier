import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import requests
from io import BytesIO
from flask import Flask, request, jsonify

app = Flask(__name__)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

class BadgeClassifier:
    def __init__(self, model_path, class_names):
        self.model = self.load_model(model_path)
        self.class_names = class_names
        self.transform = self.get_transform()

    def load_model(self, model_path):
        model = models.squeezenet1_1(pretrained=False)
        model.num_classes = 20
        model.classifier._modules["1"] = nn.Conv2d(512, model.num_classes, kernel_size=(1, 1))
        model.load_state_dict(torch.load(model_path))
        model.eval()
        model.to(device)
        return model

    def get_transform(self):
        transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
        return transform

    def classify_image(self, image_path):
        image = Image.open(image_path).convert('RGB')
        image = self.transform(image).unsqueeze(0).to(device)
        with torch.no_grad():
            output = self.model(image)
            probabilities = torch.softmax(output, dim=1)[0]
            predicted_idx = torch.argmax(probabilities).item()
            predicted_label = self.class_names[predicted_idx]
            confidence = probabilities[predicted_idx].item()
        return predicted_label, confidence

    def classify_image_url(self, image_url):
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content)).convert('RGB')
        image = self.transform(image).unsqueeze(0).to(device)
        with torch.no_grad():
            output = self.model(image)
            probabilities = torch.softmax(output, dim=1)[0]
            predicted_idx = torch.argmax(probabilities).item()
            predicted_label = self.class_names[predicted_idx]
            confidence = probabilities[predicted_idx].item()
        return predicted_label, confidence


model_path = "model/model.pth"
class_names = ['arsenal', 'aston-villa', 'brentford', 'brighton', 'burnley', 'chelsea', 'crystal-palace', 'everton', 'leeds', 'leicester-city',
               'liverpool', 'manchester-city', 'manchester-united', 'newcastle', 'norwich', 'southampton', 'tottenham', 'watford', 'west-ham',
                'wolves']  

classifier = BadgeClassifier(model_path, class_names)


@app.route('/classify', methods=['POST'])
def classify_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file uploaded'}), 400

    image = request.files['image']
    image.save('temp.jpg')  

    predicted_label, confidence = classifier.classify_image('temp.jpg')

    return jsonify({'predicted_label': predicted_label, 'confidence': confidence})


@app.route('/classify_url', methods=['POST'])
def classify_image_url():
    if 'url' not in request.json:
        return jsonify({'error': 'No image URL provided'}), 400

    image_url = request.json['url']

    predicted_label, confidence = classifier.classify_image_url(image_url)

    return jsonify({'Logo': predicted_label})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9696)
