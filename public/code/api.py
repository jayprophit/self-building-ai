import os
from fastapi import FastAPI
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise RuntimeError("OpenAI API Key not found in environment variables.")

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Self-Building AI!"}

@app.post("/fix_error/")
def fix_error(error_message: str):
    """
    API endpoint to fix errors using OpenAI
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Fix the following error: {error_message}",
            max_tokens=100
        )
        fix = response.choices[0].text.strip()
        return {"suggested_fix": fix}
    except Exception as e:
        return {"error": str(e)}
