from fastapi import FastAPI
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/generate_text")
def generate_text(prompt: str):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return {"generated_text": response.choices[0].text.strip()}
