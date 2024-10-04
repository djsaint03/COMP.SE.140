# Dockerfile for Service2 (Node.js)
FROM node:14

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY service2.js /app/service2.js

CMD ["node", "service2.js"]