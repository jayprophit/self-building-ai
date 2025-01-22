# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install TensorFlow (if it's not included in requirements.txt)
RUN pip install tensorflow

# Install cron job manager
RUN apt-get update && apt-get install -y cron

# Expose the port the app runs on
EXPOSE 8000

# Run Cron job to execute self_iteration.py every hour
RUN (crontab -l ; echo "0 * * * * python /app/private/code/self_iteration.py") | crontab -

# Run the application (using uvicorn to run the FastAPI app)
CMD ["uvicorn", "public.code.api:app", "--host", "0.0.0.0", "--port", "8000"]
