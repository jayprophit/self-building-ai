# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install TensorFlow (if you don't have it in requirements.txt)
RUN pip install tensorflow

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["uvicorn", "public.code.api:app", "--host", "0.0.0.0", "--port", "8000"]