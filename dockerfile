# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install required Python libraries
RUN pip install -r requirements.txt

# Define the entry point for the container
CMD ["python", "private/code/main.py"]