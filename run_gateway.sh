echo "Delete existing API Gateway container"

docker stop apigateway
docker rm apigateway

echo "Delete existing API Gateway image"

docker rmi apigateway

echo "Build image API Gateway"

docker build -t apigateway .

echo "running docker..."

docker run -d --name apigateway --network perfectpicknetwork -p 9000:9000 apigateway 

