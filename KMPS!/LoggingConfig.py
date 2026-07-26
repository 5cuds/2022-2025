from FileManagement import FileManager
import logging
import datetime
import os


def Log(name: str) -> None:
    """Function To Set Up A Logger"""

    formatter = logging.Formatter('[%(asctime)s|%(name)s] [%(levelname)s]: %(message)s')
    logger = logging.getLogger(name)

    path = os.path.join(FileManager().path(), "Logs", f"KMPS! Log - {datetime.date.today()}.log")
    
    # Check if the logger already has handlers to avoid duplicates
    if not logger.handlers:
        handler = logging.FileHandler(path)
        handler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)

    return logger