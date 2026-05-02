import logging
import os

def setup_logging():
    """Sets up logging to both console and a file."""
    log_file = "trading_bot.log"
    
    # Create logger
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.INFO)
    
    # Create formatters
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_formatter = logging.Formatter('%(levelname)s: %(message)s')
    
    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(file_formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)
    
    # Add handlers to logger
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger

# Initialize logger
logger = setup_logging()
