import os
import logging
import openai
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise RuntimeError("OpenAI API Key not found in environment variables.")


# Setup logging
LOG_FILE = './private/logs/self_iteration.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Directory for logs
LOG_DIR = "./private/logs/"
ERROR_LOG_FILE = os.path.join(LOG_DIR, "error.log")
FIXED_CODE_FILE = "./private/code/main.py"  # The file where fixes are applied

def analyze_logs():
    """
    Analyze the logs for errors.
    """
    if not os.path.exists(ERROR_LOG_FILE):
        logging.warning(f"Log file not found: {ERROR_LOG_FILE}")
        return []

    with open(ERROR_LOG_FILE, "r") as f:
        logs = f.readlines()
        errors = [log.strip() for log in logs if "ERROR" in log]
        if errors:
            logging.info(f"Found {len(errors)} error(s) in the log.")
        return errors

def generate_fix(error_message):
    """
    Use OpenAI to generate a fix for a given error message.
    """
    prompt = f"Fix the following error: {error_message}"
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        fix = response.choices[0].text.strip()
        logging.info(f"Generated fix for error: {error_message}")
        return fix
    except Exception as e:
        logging.error(f"Error generating fix for '{error_message}': {str(e)}")
        return None

def apply_fix(file_path, fix_message):
    """
    Append the fix to the specified file.
    """
    try:
        with open(file_path, "a") as f:
            f.write(f"\n# Fix applied: {datetime.now()}\n")
            f.write(fix_message + "\n")
        logging.info(f"Applied fix to {file_path}")
    except Exception as e:
        logging.error(f"Failed to apply fix to {file_path}: {str(e)}")

def self_iterate():
    """
    Main function to analyze logs, generate fixes, and apply them.
    """
    errors = analyze_logs()
    if errors:
        for error in errors:
            logging.info(f"Found error: {error}")
            fix = generate_fix(error)
            if fix:
                logging.info(f"Suggested fix: {fix}")
                apply_fix(FIXED_CODE_FILE, fix)
            else:
                logging.warning(f"No fix generated for error: {error}")
    else:
        logging.info("No errors found. System is up to date.")

if __name__ == "__main__":
    logging.info("Starting self-iteration process.")
    self_iterate()
    logging.info("Self-iteration process completed.")
