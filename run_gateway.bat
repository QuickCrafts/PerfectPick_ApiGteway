@echo off

rem Delete existing apigateway container
docker stop apigateway
docker rm apigateway

rem Delete existing apigateway image
docker rmi apigateway

rem Build apigateway image
docker build -t apigateway .

rem Create apigateway container
docker run -d --name apigateway --network mynetwork -p 9000:9000 apigateway 