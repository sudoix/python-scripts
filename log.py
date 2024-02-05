import logging

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S:%z:%s',
    filename='%slog' % __file__,
    filemode='w') # CHANGE DEFAULT TO DEBUG, INFO, WARNING, ERROR, CRITICAL

username = 'Milad'

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message from %s" % username)

a = 2
b = 0

try:
    c = a/b
except Exception as e:
    logging.error("Error occurred", exc_info=True)
