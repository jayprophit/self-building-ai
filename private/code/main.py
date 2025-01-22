import os
import openai
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise RuntimeError("OpenAI API Key not found in environment variables.")

# Setup logging
LOG_FILE = './private/logs/main.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main function to run the self-building AI.
    """
    try:
        logging.info("Running the main process.")
        
        # Example: Generate a simple completion from OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="Hello, world!",
            max_tokens=5
        )
        logging.info(f"OpenAI response: {response.choices[0].text.strip()}")
        
        # Add any other process here (e.g., training, analyzing data, etc.)

    except Exception as e:
        logging.error(f"Error during execution: {str(e)}")

if __name__ == "__main__":
    main()
