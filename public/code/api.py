from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import openai
import os

# Load environment variables
load_dotenv()

# Initialize the FastAPI app
app = FastAPI()

# Load OpenAI API Key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OpenAI API Key not found in environment variables.")
openai.api_key = OPENAI_API_KEY

# Root endpoint
@app.get("/")
def read_root():
    """
    Root endpoint for the Self-Building AI API.
    """
    return {"message": "Welcome to the Self-Building AI API"}

# Fix code endpoint
@app.post("/fix_code")
def fix_code(error_message: str):
    """
    Endpoint to receive an error message, request a fix from OpenAI, and return the fix.
    """
    if not error_message:
        raise HTTPException(status_code=400, detail="Error message is required.")
    
    try:
        # Request a fix for the error message from OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",  # Specify the model to use
            prompt=f"Fix the following error: {error_message}",
            max_tokens=100  # Limit the response length
        )
        
        # Get the suggested fix
        fix = response.choices[0].text.strip()
        
        # Return the original error message and the suggested fix
        return {"error_message": error_message, "fix": fix}
    
    except Exception as e:
        # If there is an issue, raise an HTTPException with the error details
        raise HTTPException(status_code=500, detail=f"Error while processing the request: {str(e)}")

# Health check endpoint
@app.get("/health")
def health_check():
    """
    Endpoint to check if the app is healthy.
    This is used by platforms like Render to check the app's status.
    """
    try:
        # Check if the OpenAI API key is available
        if not openai.api_key:
            raise RuntimeError("OpenAI API key is not set.")
        
        # If everything is fine, return a healthy status
        return {"status": "healthy"}
    
    except Exception as e:
        # If there is an issue, raise an HTTPException with the health check failure message
        raise HTTPException(status_code=500, detail=f"Health check failed: {str(e)}")
