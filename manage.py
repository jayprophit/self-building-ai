import os
import sys
from dotenv import load_dotenv

def check_env_vars():
    """
    Check if the required environment variables are set.
    """
    load_dotenv()  # Load environment variables from a .env file

    required_vars = ["OPENAI_API_KEY", "DATABASE_URL"]  # Add more as needed
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        print(f"Error: Missing required environment variables: {', '.join(missing_vars)}")
        sys.exit(1)  # Exit with a non-zero status to indicate failure

    print("All required environment variables are set.")

def run_pre_deploy_tasks():
    """
    Run tasks that should be completed before deployment.
    """
    print("Running pre-deploy tasks...")

    # Check for environment variables
    check_env_vars()

    # Add more pre-deploy tasks here if needed (e.g., migrations, static files collection)

    print("Pre-deploy tasks completed successfully.")

def main():
    """
    Main function to handle the pre-deploy process.
    """
    run_pre_deploy_tasks()

if __name__ == "__main__":
    main()
