#!/bin/bash

# Exit on error
set -e

# Pull the latest changes from GitHub
echo "Pulling the latest changes from GitHub..."
git pull origin main

# Build and run the Docker container
echo "Building and running the Docker container..."
docker-compose -f .devcontainer/docker-compose.yml up --build -d

# Run any pre-deploy tasks (if any)
if [ -f "scripts/pre_deploy.py" ]; then
    echo "Running pre-deploy tasks..."
    python3 scripts/pre_deploy.py
else
    echo "No pre-deploy tasks found."
fi

# Check if the application is running
echo "Checking if the application is running..."
if curl --silent --fail http://localhost:8000/health; then
    echo "Application is running successfully."
else
    echo "Health check failed. Deployment unsuccessful."
    exit 1
fi

echo "Deployment completed successfully."
