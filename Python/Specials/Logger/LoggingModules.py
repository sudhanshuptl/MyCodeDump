import logging
from logging.handlers import TimedRotatingFileHandler


logger=logging.getLogger(__name__)

file_handler = TimedRotatingFileHandler('MyLog.log', when='midnight', interval=1)
file_handler.suffix = '%d%m%Y'

formatter=logging.Formatter('%(process)d:%(module)s:%(funcName)s:%(lineno)d:%(asctime)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel('INFO')

