FROM registrysecaas.azurecr.io/secaas/python:3-latest

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip
user root
RUN apk add --no-cache --virtual .build-deps gcc musl-dev
RUN pip install -r requirements.txt
user python
CMD ["python", "app.py"]


