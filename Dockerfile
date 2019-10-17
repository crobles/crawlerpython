FROM registrysecaas.azurecr.io/secaas/python:3-latest

WORKDIR /app

ADD . /app

USER root

RUN pip install --upgrade pip

RUN apk add --no-cache --virtual .build-deps gcc musl-dev

RUN pip install -r requirements.txt

USER python

CMD ["python", "app.py"]


