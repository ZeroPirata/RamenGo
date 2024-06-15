from logging import getLogger, ERROR, INFO, DEBUG,  FileHandler, Formatter
from src.config.settings import settings

global LOGGER
LOGGER = getLogger()
LOGGER.setLevel(DEBUG)
LOGGER.setLevel(ERROR)
LOGGER.setLevel(DEBUG)
LOGGER.setLevel(INFO)

log_path = settings.PATH_LOGGER

if log_path:
    handler = FileHandler(log_path)
    formatter = Formatter("[%(asctime)s] [%(levelname)s] - %(message)s")
    handler.setFormatter(formatter)
    LOGGER.addHandler(handler)
