#!/bin/bash

# Pull the latest changes from GitHub
git pull origin main

# Build and run the Docker container
docker-compose up --build -d

# Run any pre-deploy tasks
python3 scripts/pre_deploy.py

# Check if the application is running
curl --silent --fail http://localhost:8000/health || exit 1

echo "Deployment completed successfully."
