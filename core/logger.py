from logging import getLogger, INFO, Formatter, StreamHandler, FileHandler
import os


def setup_logger():
    # create folder for log storage
    os.makedirs(name='logs', exist_ok=True)

    # set up looger
    # create a logger instance
    logger = getLogger(name='ETFPremiumTracker')

    # set info level
    logger.setLevel(level=INFO)

    # logs formatting
    formatter = Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

    # handlers
    # to avoid duplicate logs or same log will be printed multiple times
    if logger.hasHandlers():
        return logger

    # create console handler
    console_handler = StreamHandler()
    console_handler.setFormatter(formatter)

    # create file handler
    file_handler = FileHandler(filename='logs/app.log',mode='a')
    file_handler.setFormatter(formatter)

    # attach handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

logger = setup_logger()








