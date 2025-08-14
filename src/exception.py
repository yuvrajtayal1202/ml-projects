import sys
from logger import logging  # ✅ uses your logger.py

def error_message_detail(error, error_detail: sys):
    """Return a detailed error message with file name, line number, and error text."""
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'Error occurred in python script named [{0}] line no. [{1}] error message[{2}]'.format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class customException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        detailed_message = error_message_detail(error_message, error_detail=error_detail)
        self.error_message = detailed_message
        
        # ✅ Log the error automatically
        logging.error(detailed_message)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by Zero attempted")
        raise customException(e, sys)
