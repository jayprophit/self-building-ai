import os
import logging
from datetime import datetime

# Set up logging configuration
def setup_logging(log_file='app.log'):
    """Set up the logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

# Log an error message
def log_error(message):
    """Log an error message."""
    logging.error(message)

# Log an info message
def log_info(message):
    """Log an info message."""
    logging.info(message)

# Check if a file exists
def file_exists(file_path):
    """Check if the file exists."""
    return os.path.exists(file_path)

# Read a configuration from an environment variable
def get_env_variable(var_name, default_value=None):
    """Get the value of an environment variable."""
    return os.getenv(var_name, default_value)

# Validate if a string is not empty
def validate_non_empty_string(value, field_name):
    """Validate if a string is not empty."""
    if not value:
        raise ValueError(f"{field_name} cannot be empty.")
    return value

# Validate if a number is positive
def validate_positive_number(value, field_name):
    """Validate if a number is positive."""
    if value <= 0:
        raise ValueError(f"{field_name} must be a positive number.")
    return value

# Format the current date in YYYY-MM-DD format
def get_current_date():
    """Get the current date in YYYY-MM-DD format."""
    return datetime.now().strftime('%Y-%m-%d')

# Save a dictionary to a file as JSON
import json
def save_dict_to_json(data, file_path):
    """Save a dictionary to a file as JSON."""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Load a dictionary from a JSON file
def load_dict_from_json(file_path):
    """Load a dictionary from a JSON file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")
    
    with open(file_path, 'r') as f:
        return json.load(f)
