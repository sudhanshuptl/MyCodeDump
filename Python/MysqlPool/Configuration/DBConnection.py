from mysql.connector.pooling import MySQLConnectionPool
import mysql.connector
from .config import MYSQL_CONFIG


class DatabasePool:
    def __init__(self, db_config):
        self.__db_config = db_config
        self._my_conn_pool = None
        self._my_conn_pool = self.create_connection(db_config)

    @staticmethod
    def create_connection(db_config):
        return MySQLConnectionPool(pool_name='mypool',
                                   pool_size=3,
                                   **db_config)

    def create_new_connection_pool(self):
        self._my_conn_pool = self.create_connection(self.__db_config)

    def get_connection(self):
        try:
            con = self._my_conn_pool.get_connection()
            return con
        except mysql.connector.errors.PoolError as e:
            print('PoOl Exhausted')
            raise OverflowError('Database Pool Exhausted')


connection_pool_obj = DatabasePool(MYSQL_CONFIG)
connection_pool_obj._my_conn_pool.
