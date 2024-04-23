docker stop apigateway
docker rm apigateway

docker rmi apigateway

docker build -t apigateway .

echo "running docker..."

docker run -d --name apigateway --network perfectpickusersnetwork -p 9000:9000 apigateway 

