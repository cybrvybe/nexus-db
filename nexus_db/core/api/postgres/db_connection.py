import psycopg2
import logging
from contextlib import contextmanager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class DbConnection:
    def __init__(self, user='postgres', password='password', host='localhost', port='5432'):
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    @contextmanager
    def connect(self, db_name='postgres'):
        conn = None
        try:
            conn = psycopg2.connect(user=self.user, password=self.password, host=self.host, port=self.port, dbname=db_name)
            yield conn
        except Exception as e:
            logging.error("Unable to connect to the database")
            logging.exception(e)
        finally:
            if conn is not None:
                conn.close()