"""General logging configuration"""
import logging
import os
import datetime
from dataclasses import dataclass
from dotenv import load_dotenv

@dataclass
class LogConf:
    """Class to handle logging configuration"""

    def __init__(self):
        load_dotenv()
        log_dir = os.getenv("LOG_DIR")
        log_level = os.getenv("LOG_LEVEL")

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        filename = f"newspipe_{self.get_timestamp()}.log"
        log_file = os.path.join(log_dir, filename)
        logging.basicConfig(filename=log_file, level=log_level)
        logging.info("Log file: %s", log_file)

    def get_timestamp(self):
        """Returns formatted timestamp for log file name"""
        date_now = datetime.datetime.now()
        return date_now.strftime("%Y%m%d_%H%M%S")
