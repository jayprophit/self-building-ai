import os
import openai
import subprocess
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_logs():
    """
    Analyze logs for errors. This function reads a log file and looks for any
    lines that contain the word 'ERROR'.
    """
    log_file = "./logs/error.log"
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            logs = f.readlines()
            return [log.strip() for log in logs if "ERROR" in log]
    return []

def get_chatgpt_fix(error_message):
    """
    Call the OpenAI API to get a fix suggestion for the error message.
    """
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # You can use other models like "gpt-4" if available
            prompt=f"Given the following error message in a Python program, suggest a code fix:\nError: {error_message}\nFix:",
            max_tokens=150,
            temperature=0.5
        )
        fix = response.choices[0].text.strip()
        return fix
    except Exception as e:
        return f"Error communicating with OpenAI API: {str(e)}"

def generate_fix(error_message):
    """
    Generate a fix for the error by calling the ChatGPT API.
    """
    fix = get_chatgpt_fix(error_message)
    return fix

def apply_fix(file_path, fix_message):
    """
    Apply the suggested fix to the file.
    This is a simple demonstration of adding a comment to the code.
    In a real system, this would be more complex and would need proper error handling and modification of the code.
    """
    try:
        with open(file_path, "a") as file:
            file.write(f"\n# Suggested Fix: {fix_message}\n")
        print(f"Fix applied to {file_path}: {fix_message}")
    except Exception as e:
        print(f"Error applying fix to {file_path}: {str(e)}")

def self_iterate():
    """
    The main self-iteration loop that reads logs, analyzes errors, and applies fixes.
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

def schedule_cron_job():
    """
    Schedules the self-iteration function to run at regular intervals using cron.
    """
    cron_command = "0 * * * * python /app/private/code/self_iteration.py"
    try:
        # Update the cron jobs and add the new job to the cron table
        current_cron_jobs = subprocess.check_output("crontab -l", shell=True).decode()
        new_cron_jobs = current_cron_jobs + f"\n{cron_command}\n"
        subprocess.run(f'echo "{new_cron_jobs}" | crontab -', shell=True)
        print("Cron job scheduled to run self_iteration.py every hour.")
    except Exception as e:
        print(f"Error scheduling cron job: {str(e)}")

if __name__ == "__main__":
    # Call the self-iteration function
    self_iterate()
    
    # Schedule the cron job (for Docker container setup)
    schedule_cron_job()
