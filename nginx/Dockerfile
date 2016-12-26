FROM nginx:1.11-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY flask-app.conf /etc/nginx/conf.d/flask-app.conf
