# English Premier League Clubs Logo Identifier by 🅱🅻🅰🆀


![image](https://github.com/Blaqadonis/epl_teams_logo_identifier/assets/100685852/ff72e5d6-e475-460e-a19c-457bf4fdc863)  









## This service:
This is a classification service. It reads an image of a football club logo and classifies it as belonging to one of the following: 


```arsenal
aston-villa
brentford
brighton
burnley
chelsea
crystal-palace
everton
leeds
leicester-city
liverpool
manchester-city
manchester-united
newcastle
norwich
southampton
tottenham
watford
west-ham
wolves
```
    
    
Data collated for these 20 clubs only.  

 


## Downloading the data:

Click the link to begin download of the zip file. Extract all contents of zip file in your local directory.

[Click Here](https://www.kaggle.com/datasets/alexteboul/english-premier-league-logo-detection-20k-images/download?datasetVersionNumber=4)


## Running this service:

This runs locally. If you want to try out the service, follow the steps below:

Before you proceed, create a virtual environment. I used ```python version 3.10.11``` 

To create an environment with that version of python using Conda: ```conda create -n <env-name> python=3.10.11```

Just replace ```<env-name>``` with any title you want. 

Next:


 ```conda activate <env-name>``` to activate the environment.


Navigate into the local folder where you extracted the zip file at. 


Clone this repository ``` git clone https://github.com/Blaqadonis/human_action_recognition_app.git ```


Run ```pip install -r requirements.txt``` to install all necessary external dependencies.



You need to have docker installed on your system. I am using a windows machine, and I have docker desktop installed on my system. 


If you do not have that then you should try doing that first. If you are all set and good, then proceed.


Now, run ```docker build -t <service-name>:v1 .```


Replace ```<service-name>``` with whatever name you wish to give to the service, to build the image.


Then run the service:    ```docker run -it --rm -p 9696:9696 <service-name>:latest```


NOTE: I am running this on Windows hence Waitress. If your local machine requires Gunicorn, I think the Dockerfile should be edited with something like this:


```
FROM python:3.10-slim-buster

RUN pip install -U pip 

WORKDIR /app

COPY [ "model.py", "model.pth", "requirements.txt", "./" ]

RUN pip install -r requirements.txt

EXPOSE 9696 

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "model:app" ]
 ```


If the container is up and running, open up a new terminal. Reactivate the Conda environment. 


Run ```python test.py```




















Try this out with family, friends, colleagues, neighbours, and let me know how to improve on it.

