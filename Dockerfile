FROM node:20-alpine
WORKDIR /app
COPY . .
EXPOSE 3000
CMD ["sh", "-c", "echo 'Docker image ready for MiddayMate'" ]
