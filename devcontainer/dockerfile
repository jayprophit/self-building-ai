# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install TensorFlow (if it's not included in requirements.txt)
RUN pip install tensorflow

# Install cron job manager and any other necessary utilities
RUN apt-get update && apt-get install -y cron

# Set environment variables for OpenAI API key and other variables
RUN echo "OPENAI_API_KEY=${OPENAI_API_KEY}" >> /app/.env

# Expose the port the app runs on
EXPOSE 8000

# Set up Cron job to execute self_iteration.py every hour
RUN (crontab -l ; echo "0 * * * * python /app/private/code/self_iteration.py") | crontab -

# Create logs directory
RUN mkdir -p /app/private/logs

# Check and prepare for any existing errors in the logs (for debugging before deploy)
RUN tail -n 10 /app/private/logs/error.log

# Pre-deploy tasks (install dependencies, check logs, and run migrations)
RUN pip install -r requirements.txt  # Ensure dependencies are installed
RUN export $(cat .env | xargs)  # Load environment variables

# Health check command to verify if the app is healthy
RUN curl --silent --fail http://localhost:8000/health || exit 1

# Run the application using uvicorn (FastAPI app)
CMD ["uvicorn", "public.code.api:app", "--host", "0.0.0.0", "--port", "8000"]
