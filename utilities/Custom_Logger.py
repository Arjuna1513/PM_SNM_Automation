import logging
import inspect
from colorama import Fore, Style

class CustomLogger:

    def custom_logger(self, logLevel=logging.INFO):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        logger.setLevel(logging.DEBUG)

        fHandler = logging.FileHandler("Automation.log", mode='a')
        fHandler.setLevel(logLevel)

        formatter = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s : %(message)s"
                                      , datefmt="%d/%m/%Y  %H:%M:%S")
        fHandler.setFormatter(formatter)
        logger.addHandler(fHandler)

        return logger
