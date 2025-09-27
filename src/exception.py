import sys

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    error_message = f"Error occurred in pyhon script name [{0}] line number {1} error me: {str(error)}"