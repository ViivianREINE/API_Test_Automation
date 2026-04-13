"""Logging utility for the API Test Automation Framework."""

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def log(message):
    """Log an info message."""
    logging.info(message)
