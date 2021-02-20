import logging
import os
from logging.handlers import RotatingFileHandler


def setup_log():
    logging.basicConfig(level=logging.INFO)
    file_log_handler = RotatingFileHandler(os.path.abspath('logs/log'), maxBytes=1024*1024*100, backupCount=100)
    formatter = logging.Formatter("%(levelname)s %(filename)s: %(lineno)d %(message)s")
    file_log_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_log_handler)
