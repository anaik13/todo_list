import logging


def configure_logger():

    logger = logging.getLogger(__name__)

    logger.setLevel(logging.INFO) # set level of logging to logger

    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('logs.log')
    c_handler.setLevel(logging.WARNING)  # save all logs >= 'WARNING'
    f_handler.setLevel(logging.INFO)  # save all logs >= 'INFO'

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(name)s - %(levelname)s xs- %(message)s') # TODO: xs
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger