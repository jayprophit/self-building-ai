import logging

# Set up the logger
logger = logging.getLogger("self_building_ai")
logger.setLevel(logging.DEBUG)  # Log everything, change to ERROR for only error logs

# Create a file handler that logs to 'error.log'
file_handler = logging.FileHandler("private/logs/error.log")
file_handler.setLevel(logging.ERROR)  # Only log errors to the file

# Create a console handler to also log to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Log info messages to the console

# Create a log formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
