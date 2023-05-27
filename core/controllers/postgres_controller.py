import psycopg2

class PostgresController:
    def add_connection(self, host_name, port, db_name, user, password):
        return psycopg2.connect(
            host=host_name,
            port=port,
            dbname=db_name,
            user=user,
            password=password
        )
    
    def add_cursor(self, connection):
        return connection.cursor()
    
    def execute_query(self, query, cursor):
        cursor.execute(query)

    def close_controller(self, cursor, connection):
        cursor.close()
        connection.close()

    
