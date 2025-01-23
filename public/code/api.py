import os
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import openai
from .database import get_db, Base, engine  # Assuming database.py is set up for SQLAlchemy

# Load environment variables
load_dotenv()

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise RuntimeError("OpenAI API Key not found in environment variables.")

# Initialize FastAPI app
app = FastAPI()

# Example of a database model
from sqlalchemy import Column, Integer, String

class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

# Create tables in the database
Base.metadata.create_all(bind=engine)

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

@app.get("/items/")
def get_items(db: Session = Depends(get_db)):
    """
    Endpoint to get items from the database
    """
    items = db.query(Item).all()  # Query the 'Item' model
    return items
