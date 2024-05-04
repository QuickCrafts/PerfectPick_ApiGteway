rem Run rabbitMQ
docker run -d --rm --name rabbitmq --network perfectpicknetwork -p 5672:5672 -p 15672:15672 rabbitmq