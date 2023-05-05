import os
import logging


class Logger:
    def __init__(self, name, level=logging.INFO):

        log_file = r"C:\Users\richard.nagy\OneDrive - Mazars in Slovakia\Pracovná plocha\Archive\diplmovka\code\logs\log.txt"
        
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)
        

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)


