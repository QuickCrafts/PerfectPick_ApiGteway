# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Make port 80 available to the world outside this container
EXPOSE 80
EXPOSE 8001
EXPOSE 5672
EXPOSE 27017


# Wait for MongoDB and RabbitMQ to be ready (timeout: 1 minute)
#CMD /wait-for-it.sh mongo:27017 --timeout=60 --strict -- \
#    /wait-for-it.sh rabbitmq:5672 --timeout=60 --strict -- \
#    uvicorn main:app --host 0.0.0.0 --port 8000

CMD uvicorn app.main:app --host 0.0.0.0 --port 8001
