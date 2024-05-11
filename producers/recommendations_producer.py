import pika
import json

def send_recommendation(recommendation_data):
    try:
        # Establish a connection to RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672))
        channel = connection.channel()

        # Declare the queue
        channel.queue_declare(queue='recommendations')

        # Convert the recommendation data to a JSON string
        message = json.dumps(recommendation_data)

        # Publish the message to the queue
        channel.basic_publish(exchange='', routing_key='recommendations', body=message)
        print(f" [x] Sent recommendation data: {message}")

    except pika.exceptions.AMQPConnectionError:
        print("Failed to connect to RabbitMQ. Please check if RabbitMQ is running.")
    finally:
        # Close the connection
        if connection:
            connection.close()

# Test the send_recommendation function with the provided recommendation data
""" recommendation_data = {
    "id_user": 245564845,
    "movies": ["tt0106941", "tt0118694"],
    "books": ["AYhxAQHUdCYC", "fyPsAAAAMAAJ"],
    "songs": ["3qhlB30KknSejmIvZZLjOD"]
}
send_recommendation(recommendation_data) """