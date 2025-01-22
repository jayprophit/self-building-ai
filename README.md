# Self-Building AI Project

## Overview

This project is designed to create an AI system capable of iterating on its own code, generating fixes for errors, and providing a self-improvement mechanism. It integrates with OpenAI's GPT models to fix errors and visualize code.

## Features

- **Code Fixer**: Enter error messages and receive code fixes.
- **Preview Area**: Visualize designs, code, and project types.
- **Self-Iteration**: The system analyzes logs, generates fixes, and applies them automatically.
- **Deployment**: The project can be deployed using Docker and includes a CI/CD pipeline for continuous integration.

## Requirements

- Python 3.9 or higher
- Docker
- Docker Compose
- OpenAI API Key

## Setup

1. Clone the repository.
2. Set up your environment:
    ```bash
    cp .env.example .env
    ```
    Add your OpenAI API key in the `.env` file.

3. Build and run the project using Docker Compose:
    ```bash
    docker-compose up --build
    ```

4. Access the app:
    - FastAPI app: `http://localhost:8000`
    - Streamlit interface: `http://localhost:8501`

## Deployment

To deploy the application, use the `deploy.sh` script:
```bash
bash scripts/deploy.sh
