import logging
import os
from datetime import datetime


def logging_config(log_dir="logs", log_level=logging.INFO):
    """Create a reusable logger configuration for the project pipeline."""
    os.makedirs(log_dir, exist_ok=True)

    current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    log_file_path = os.path.join(log_dir, f"log_{current_time}.log")

    logger = logging.getLogger("ml_project_logger")
    logger.setLevel(log_level)
    logger.propagate = False

    if logger.handlers:
        logger.handlers.clear()

    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")

    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


logger = logging_config()


if __name__ == "__main__":
    logger.info("Logger initialized successfully.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
