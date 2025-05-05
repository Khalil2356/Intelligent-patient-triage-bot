import logging
import os

def setup_logger():
    logger = logging.getLogger("TriageBot")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        handler = logging.FileHandler("app/triage_bot.log")
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger