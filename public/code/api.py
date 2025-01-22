from fastapi import FastAPI, HTTPException
import os
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

# Initialize the FastAPI app
app = FastAPI()

# Load OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OpenAI API Key not found in environment variables.")
openai.api_key = OPENAI_API_KEY

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Self-Building AI API"}

# Fix code endpoint
@app.post("/fix-code/")
def fix_code(error_message: str):
    """
    Endpoint to generate a fix for a given error message using OpenAI's API.
    """
    if not error_message:
        raise HTTPException(status_code=400, detail="Error message is required.")
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Fix the following error: {error_message}",
            max_tokens=100
        )
        fix = response.choices[0].text.strip()
        return {"error_message": error_message, "fix": fix}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Health check endpoint
@app.get("/health")
def health_check():
    """
    Endpoint to check if the app is healthy.
    This is used by Render to check the app's status.
    """
    try:
        # Check if the OpenAI API key is available
        if not openai.api_key:
            raise RuntimeError("OpenAI API key is not set.")
        return {"status": "healthy"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Health check failed: {str(e)}")
