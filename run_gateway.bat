@echo off

docker build -t apigateway .
docker run -d --name apigateway -p 9000:9000 apigateway