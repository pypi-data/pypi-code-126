import logging

# Adding logger to the module

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s (%(funcName)s): %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

file_handler = logging.FileHandler('cobrseo.log', mode='w')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

root_logger.addHandler(file_handler)
