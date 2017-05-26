FROM python:3.4.5-wheezy

RUN mkdir -p /app/src
COPY ./requirements.txt /app
WORKDIR /app/src

RUN pip install -r /app/requirements.txt

CMD ["python", "./app.py"]
