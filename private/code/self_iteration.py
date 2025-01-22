import os
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_logs():
    """
    Analyze the logs for errors.
    """
    log_file = "./private/logs/error.log"
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            logs = f.readlines()
            return [log.strip() for log in logs if "ERROR" in log]
    return []

def generate_fix(error_message):
    """
    Use OpenAI to generate a fix for a given error message.
    """
    prompt = f"Fix the following error: {error_message}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def apply_fix(file_path, fix_message):
    """
    Append the fix to the specified file.
    """
    with open(file_path, "a") as f:
        f.write("\n# Fix applied:\n")
        f.write(fix_message + "\n")

def self_iterate():
    """
    Main function to analyze logs, generate fixes, and apply them.
    """
    errors = analyze_logs()
    if errors:
        for error in errors:
            print(f"Found error: {error}")
            fix = generate_fix(error)
            print(f"Suggested fix: {fix}")
            apply_fix("./private/code/main.py", fix)
    else:
        print("No errors found. System is up to date.")

if __name__ == "__main__":
    self_iterate()
