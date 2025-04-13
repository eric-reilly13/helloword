FROM python:3.9-slim-buster

# Install curl and bash
RUN apt-get update && apt-get install -y curl bash

# Set working directory inside the container
WORKDIR /app

# Copy your Python app code into the container
COPY app/app.py .

# Install Flask
RUN pip install Flask

# Expose port 80 to be able to access it
EXPOSE 80

# Set environment variable to tell Flask to listen on all interfaces
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run the Flask app
CMD ["python", "app.py"]