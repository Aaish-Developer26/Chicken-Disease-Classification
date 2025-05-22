import logging
import sys
import os

logging_str = "{%(asctime)s}: %(levelname)s: %(module)s: %(message)s}"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,

    handlers = [
        logging.FileHandler(log_filepath),#To create the log File.
        logging.StreamHandler(sys.stdout) #To print the log on terminal.
    ]
)

logger = logging.getLogger("CnnClassifierLogger")
