FROM python:3.4.5-wheezy

RUN mkdir /app
ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "python", "./app.py" ]
