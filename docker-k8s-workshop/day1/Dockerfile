# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install flask

# Expose port 8080
EXPOSE 8080

# Make the script executable
CMD ["python", "guess_game.py"]