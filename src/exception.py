import sys

from src.logger import logger


class CustomException(Exception):
    """Custom exception class for better error reporting."""

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
        logger.error(self.error_message)

    def __str__(self):
        return self.error_message


def error_message_detail(error_message, error_detail: sys):
    """Return a formatted error message with file name and line number."""
    exc_tb = None

    if hasattr(error_detail, "exc_info"):
        _, _, exc_tb = error_detail.exc_info()

    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        error_text = str(error_message)
        return f"Error occurred in script: [{file_name}] at line [{line_number}] -> {error_text}"

    return str(error_message)
