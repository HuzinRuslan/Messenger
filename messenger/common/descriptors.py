"""Server port check descriptor"""

import logging

SERVER_LOGGER = logging.getLogger('server_log')


class ServerPortCheck:
    """Server port check class"""
    def __set__(self, instance, value):
        if not 1024 < value < 65535:
            SERVER_LOGGER.critical(
                f'Попытка запуска сервера с указанием неподходящего порта {value}.'
                f' Допустимы адреса с 1024 до 65535.')
            exit(1)
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name
