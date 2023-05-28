from .postgres.table_manager import TableManager
from .postgres.schema_manager import SchemaManager

def get_table_manager(request, db_connection):
    db_name = request.json.get('db_name')
    schema_name = request.json.get('schema_name')
    table_manager = TableManager(db_connection, db_name, schema_name)
    return table_manager

def get_schema_manager(request, db_connection):
    db_name = request.json.get('db_name')
    schema_manager = SchemaManager(db_connection, db_name)
    return schema_manager