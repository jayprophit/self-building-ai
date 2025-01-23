import os
import openai
import mlflow
import joblib
import logging
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
from .database import get_db, Base, engine  # Assuming database.py is set up for SQLAlchemy

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

# Initialize FastAPI app
app = FastAPI()

# Mount static files (serve files from the "public/static" directory)
app.mount("/static", StaticFiles(directory="public/static"), name="static")

# Initialize MLflow (or any other MLOps tool)
mlflow.set_tracking_uri("file:./mlruns")
mlflow.set_experiment("self-building-ai")

# Example of a database model
class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Load or register model
MODEL_PATH = './private/models/your_model.pkl'

def load_model():
    """
    Load the model from disk.
    """
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        logging.info("Model loaded successfully.")
        return model
    else:
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}")

@app.get("/")
def read_root():
    logging.info("Root endpoint hit.")
    return {"message": "Welcome to the Self-Building AI!"}

@app.post("/fix_error/")
def fix_error(error_message: str):
    """
    API endpoint to fix errors using OpenAI
    """
    try:
        logging.info(f"Received error message: {error_message}")
        
        # Generate fix suggestion using OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Fix the following error: {error_message}",
            max_tokens=100
        )
        fix = response.choices[0].text.strip()
        
        logging.info(f"OpenAI response: {fix}")
        return {"suggested_fix": fix}
    
    except Exception as e:
        logging.error(f"Error during processing: {str(e)}")
        return {"error": str(e)}

@app.post("/train_model/")
def train_model():
    """
    API endpoint to train the machine learning model.
    """
    try:
        logging.info("Starting model training.")
        
        # Example model training process
        # For demonstration, let's use a simple scikit-learn model
        from sklearn.datasets import load_iris
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import accuracy_score
        
        # Load dataset
        data = load_iris()
        X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
        
        # Train model
        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        
        # Evaluate model
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        logging.info(f"Model training complete. Accuracy: {accuracy}")
        
        # Save model using joblib
        joblib.dump(model, MODEL_PATH)
        
        # Log model to MLflow
        with mlflow.start_run():
            mlflow.log_param("model", "RandomForestClassifier")
            mlflow.log_metric("accuracy", accuracy)
            mlflow.log_artifact(MODEL_PATH)
        
        return {"message": "Model trained successfully.", "accuracy": accuracy}
    
    except Exception as e:
        logging.error(f"Error during model training: {str(e)}")
        raise HTTPException(status_code=500, detail="Model training failed")

@app.get("/predict/")
def predict(input_data: list):
    """
    API endpoint to make predictions using the trained model.
    """
    try:
        model = load_model()
        
        # Example prediction
        prediction = model.predict([input_data])
        return {"prediction": prediction.tolist()}
    
    except Exception as e:
        logging.error(f"Error during prediction: {str(e)}")
        return {"error": str(e)}

@app.get("/items/")
def get_items(db: Session = Depends(get_db)):
    """
    Endpoint to get items from the database
    """
    items = db.query(Item).all()  # Query the 'Item' model
    return items

def main():
    """
    Main function to run the self-building AI process.
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
        
        # Add any other processes here (e.g., training, analyzing data, etc.)

    except Exception as e:
        logging.error(f"Error during execution: {str(e)}")

if __name__ == "__main__":
    main()
