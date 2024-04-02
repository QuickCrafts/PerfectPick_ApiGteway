@echo off

docker build -t apigateway .
docker run -d --name apigateway -p 8001:8001 apigateway