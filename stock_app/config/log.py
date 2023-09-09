import logging

FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LEVEL = "INFO"

logging.basicConfig(format=FORMAT, level=LEVEL)


def get_logger(name):
    return logging.getLogger(name)
