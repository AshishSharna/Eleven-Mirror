from bot.helper.ext_utils.bot_utils import get_readable_file_size, MirrorStatus, get_readable_time
from telegram.message import Message
from time import time

class ZipStatus:
    def __init__(self, name, path, size):
        self.__name = name
        self.__path = path
        self.__size = size

    def progress(self):
        return '0'

    def speed(self):
        return '0'

    def name(self):
        return self.__name

    def path(self):
        return self.__path

    def size(self):
        return get_readable_file_size(self.__size)

    def eta(self):
        return '0s'

    def status(self):
        return MirrorStatus.STATUS_ARCHIVING

    def processed_bytes(self):
        return 0

    def eta(self):
        return get_readable_time(self.__info.eta)

    def message(self):
        return Message(self.__message)

    def date(self):
        return(self.__date)