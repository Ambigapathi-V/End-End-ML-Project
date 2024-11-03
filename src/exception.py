import sys
import logging
def error_message_detail(error, error_detail: sys) -> str:
    """
    Generates a detailed error message.
    
    Args:
        error: The exception that was raised.
        error_detail: The sys module to access traceback information.

    Returns:
        str: A formatted error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        "Error occurred in python script name [{0}] "
        "line number [{1}] error message [{2}]"
    ).format(file_name, exc_tb.tb_lineno, str(error))
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message: str, error_details: sys):
        super().__init__(error_message)  # Fixed super call
        self.error_message = error_message_detail(error_message, error_detail=error_details)
        
    def __str__(self):
        return self.error_message


