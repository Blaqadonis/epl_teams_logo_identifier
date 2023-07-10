FROM python:3.10-slim-buster

RUN pip install -U pip

WORKDIR /app

COPY [ "model.py", "model.pth", "requirements.txt", "./" ]

RUN pip install -r requirements.txt
EXPOSE 9696

ENTRYPOINT [ "waitress-serve", "--listen=0.0.0.0:9696", "model:app" ]