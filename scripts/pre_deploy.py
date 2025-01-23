import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup logging
LOG_FILE = './private/logs/pre_deploy.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def pre_deploy():
    """
    Pre-deployment tasks such as loading configurations and checking prerequisites.
    """
    try:
        logging.info("Starting pre-deployment checks.")
        
        # Check if .env file exists
        if not os.path.exists(".env"):
            raise FileNotFoundError(".env file not found.")
        
        logging.info("Pre-deployment checks passed successfully.")
    
    except Exception as e:
        logging.error(f"Pre-deployment failed: {str(e)}")
        raise

if __name__ == "__main__":
    pre_deploy()
