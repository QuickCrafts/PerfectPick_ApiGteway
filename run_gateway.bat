@echo off

rem Delete existing apigateway container
docker stop apigateway
docker rm apigateway

rem Delete existing apigateway image
docker rmi apigateway
docker run -d --rm --name rabbitmq --network perfectpicknetwork -p 5672:5672 -p 15672:15672 rabbitmq

rem Build apigateway image
docker build -t apigateway .

rem Create apigateway container
docker run -d --name apigateway --network perfectpicknetwork -p 9000:9000 apigateway 