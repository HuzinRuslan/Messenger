import os
import sys
import logging.handlers

sys.path.append('../../')

from common.vars import LOGGING_LEVEL, LOG_DIR_NAME, LOG_SERVER_FILE_NAME

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', LOG_DIR_NAME, LOG_SERVER_FILE_NAME)

LOG = logging.getLogger('server_log')
LOG.setLevel(LOGGING_LEVEL)

STREAM_HANDLER = logging.StreamHandler(sys.stderr)
FILE_HANDLER = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when='D')

FORMATTER = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(message)s ")

STREAM_HANDLER.setFormatter(FORMATTER)
FILE_HANDLER.setFormatter(FORMATTER)

LOG.addHandler(STREAM_HANDLER)
LOG.addHandler(FILE_HANDLER)

if __name__ == '__main__':
    LOG.critical('Критическая ошибка')
    LOG.error('Ошибка')
    LOG.debug('Отладочная информация')
    LOG.info('Информационное сообщение')
