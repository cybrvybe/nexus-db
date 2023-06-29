from ...core.api.db_direct_access_point import DbDirectAccessPoint

class CrossAppDbInterface:
    def __init__(self, schema_name: str, db_interface: DbDirectAccessPoint = None):
        self.db_interface = db_interface or DbDirectAccessPoint()
        self.schema_name = schema_name

    def init_db(self, schemas):
        for schema in schemas:
            schema_name = schema["name"]
            tables = schema["tables"]

            self.create_schema(schema_name=schema_name)
            self.create_tables_in_schema(tables=tables, schema_name=schema_name)

    def create_schemas(self, schema_names):
        for schema_name in schema_names:
            self.create_schema(schema_name=schema_name)

    def create_schema(self, schema_name):
        self.db_interface.create_schema(schema_name=schema_name)

    def create_tables_in_schema(self, tables: list, schema_name):
        self.db_interface.create_tables(schema_name=schema_name, tables=tables)

    def create_new_table(self, table_name: str, table_columns: dict):
        return self.db_interface.create_and_log_table(
            schema_name=self.schema_name,
            table_name=table_name,
            table_columns=table_columns
        )
