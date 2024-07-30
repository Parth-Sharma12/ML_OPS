import sys
from src.logger import logging
def error_message_detail(error,error_detail:sys):
    _,_, ex_tab  = error_detail.exc_info();
    filename = ex_tab.tb_frame.f_code.co_filename
    error_message = "Error in python code in file {[1]} in the line number {[2]} with error {[3]}".format(
        filename, ex_tab.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1/0;
    except Exception as e :
        logging.info("divide by zero")
        raise CustomException(e,sys)