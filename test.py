# URL classification
import requests
import json
url_url = 'http://localhost:9696/classify_url'
url = 'https://i2-prod.manchestereveningnews.co.uk/incoming/article25890577.ece/ALTERNATES/s1200c/0_chelsea.jpg'  

payload = {'url': url}
headers = {'Content-Type': 'application/json'}

response = requests.post(url_url, data=json.dumps(payload), headers=headers)
data = json.loads(response.text)
print(data)






# File classification
#file_url = 'http://localhost:9696/classify'
#file_path = 'path/to/your/image.jpg'  # Replace with the path to your image file

#files = {'image': open(file_path, 'rb')}
#response = requests.post(file_url, files=files)
#data = json.loads(response.text)
#print(data)
