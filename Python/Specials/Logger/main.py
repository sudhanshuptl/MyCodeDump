from LoggingModules import logger as log


def info():
    log.info('Inside Info Function')


def warning():
    log.warning('Inside warning Function')


def critical():
    log.critical('Inside critical Function')


def error():
    log.error('Inside error Function')


def debug():
    log.debug('Inside debug Function')


if __name__ == '__main__':
    info()
    warning()
    critical()
    error()
    debug()
    log.warning('Updating my llog level to warning ')
    log.warning('Previously it was info')
    info()
    warning()
    critical()
    error()
    debug()
