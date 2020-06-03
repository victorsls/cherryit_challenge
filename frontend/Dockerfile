FROM node:12.13.0

WORKDIR /app

COPY package.json . 
COPY package-lock.json .
RUN npm install -g @ionic/cli 
RUN npm install

COPY . .

EXPOSE 4200

CMD ["bash", "docker-entrypoint.sh"]