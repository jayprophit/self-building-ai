import os
import openai
import subprocess

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_logs():
    # Analyze logs for errors
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
    In a real system, this would be more complex.
    """
    with open(file_path, "a") as file:
        file.write(f"\n# Suggested Fix: {fix_message}\n")
    print(f"Fix applied to {file_path}: {fix_message}")

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

if __name__ == "__main__":
    self_iterate()