# thread connection
import logging
import logging.config
# core database
import sqlite3
from os.path import dirname, join

# import setting
from setting import Setting


class Connection:

    def __init__(self):
        self.__setting = Setting()
        logs_path = join(dirname(__file__), self.__setting.load_config['log']['path'])
        logging.config.fileConfig(fname=logs_path, disable_existing_loggers=False)
        # Get the logger specified in the file
        self.logger = logging.getLogger(__name__)

    def db_conn(self) -> object:
        """Get postgres sql connection
        :return: object
        """
        return sqlite3.connect(join(dirname(__file__), self.__setting.load_config['db']['path']))

    @property
    def get_config(self):
        """Load configuration from file
        :return:
        """
        return self.__setting.load_config
