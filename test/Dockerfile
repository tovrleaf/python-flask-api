FROM node:7.3-wheezy

RUN mkdir -p /tests/src
COPY package.json /tests
WORKDIR /tests

RUN npm install
CMD ["tail", "-f", "/dev/null"]
