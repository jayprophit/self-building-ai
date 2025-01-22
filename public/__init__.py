# __init__.py

# Import necessary components from modules
from .utils import (
    setup_logging,
    log_error,
    log_info,
    file_exists,
    get_env_variable,
    validate_non_empty_string,
    validate_positive_number,
    get_current_date,
    save_dict_to_json,
    load_dict_from_json
)

from .training import (
    load_training_data,
    train_model,
    suggest_fix,
    add_to_training_data
)

from .api import app  # Assuming you have a FastAPI app instance in the api.py file

# Set up any initial configuration or state
def initialize():
    """Initialize the project settings or configurations."""
    # You can add any initialization code here if needed
    log_info("Initializing the Self-Building AI project...")
