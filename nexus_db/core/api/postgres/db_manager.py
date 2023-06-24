import psycopg2
import logging
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class DbManager:

    def __init__(self, db_conn):
        self.db_conn = db_conn

    def create_db(self, db_name):
        with self.db_conn.connect() as conn:
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = conn.cursor()
            cursor.execute(f'CREATE DATABASE {db_name}')
            conn.commit()
        logging.info(f'Database {db_name} created successfully')

    def update_db_information(self, db_name):
        # Depends on what kind of information you want to update.
        pass

    def backup_db(self, db_name):
        # You can use the pg_dump tool to create a backup of your database.
        pass

    def restore_from_backup(self, backup_file_path):
        # You can use the psql tool to restore a backup of your database.
        pass

    def delete_db(self, db_name, password):
        if password == self.password:
            conn = self._connect()
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = conn.cursor()
            cursor.execute(f'DROP DATABASE IF EXISTS {db_name}')
            conn.commit()
            cursor.close()
            conn.close()
