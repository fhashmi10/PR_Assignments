"""defining logger"""
import os
import sys
import logging

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
log_filepath = os.path.join(LOG_DIR, "running_logs.log")

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]")

logger = logging.getLogger("logger")

sys.tracebacklimit=0
