import logging

class TableManager:
    def __init__(self, db_conn, db_name, schema_name):
        self.db_conn = db_conn
        self.db_name = db_name
        self.schema_name = schema_name

    def create_table(self, table_name):
        with self.db_conn.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f'CREATE TABLE {self.schema_name}.{table_name} (id SERIAL PRIMARY KEY)')
            conn.commit()
        logging.info(f'Table {table_name} created successfully in schema {self.schema_name}')

    def update_table(self, table_name):
        # Depends on what kind of update you want to make.
        pass

    def delete_table(self, table_name):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(f'DROP TABLE IF EXISTS {self.schema_name}.{table_name}')
        conn.commit()
        cursor.close()
        conn.close()

    def add_row(self, table_name, column_name_value_dict):
        conn = self._connect()
        cursor = conn.cursor()
        columns = ', '.join(column_name_value_dict.keys())
        values = ', '.join(column_name_value_dict.values())
        cursor.execute(f'INSERT INTO {self.schema_name}.{table_name} ({columns}) VALUES ({values})')
        conn.commit()
        cursor.close()
        conn.close()

    def add_column(self, table_name, column_name, data_type):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(f'ALTER TABLE {self.schema_name}.{table_name} ADD COLUMN {column_name} {data_type}')
        conn.commit()
        cursor.close()
        conn.close()
