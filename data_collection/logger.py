"""
Logger configuration for the project.
"""

import logging


def setup_logger():
    """
    Configure logging for the project.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler("scraping.log"), logging.StreamHandler()],
    )
    logging.info("Logger initialized.")
