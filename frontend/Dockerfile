FROM node:18-alpine

WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm install

COPY . .

EXPOSE 5173
# ponytail: bare vite dev server mapping to host for containerized testing
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]