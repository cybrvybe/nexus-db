import requests
from util_scripts.logs.log_handler import LogHandler

class NexusDbInterface: 
    def __init__(self):
        self.nexus_db_api_url = "http://127.0.0.1:5000"
        self.logger = LogHandler()

    def get_request_url(self, end_slugs):
        return f"{self.nexus_db_api_url}{end_slugs}"
    
    def create_db(self, db_name):
        input_json = {
            "db_name": str(db_name) if db_name else None
        }
        response = requests.post(self.get_request_url("/database/create"), json=input_json)
        self.logger.log_info(f"{db_name} database creation response: {response.json()}")
    
    def create_schema(self, schema_name):
        input_json = {
            "schema_name": str(schema_name) if schema_name else None
        }
        print("schema crreartuib")
        response = requests.post(self.get_request_url("/schema/create"), json=input_json)

    def create_table(self, schema_name, table_name, table_columns):
        print("creating table")
        table_columns = self.merge_dict(self.get_meta_table_columns(), table_columns)
        input_json = {
            "schema_name": str(schema_name) if schema_name else None,
            "table_name": str(table_name) if table_name else None,
            "table_columns": table_columns
        }
        response = requests.post(self.get_request_url("/table/create"), json=input_json)
        self.logger.log_info(f"Table {schema_name}.{table_name} creation response: {response.json()}")

        return response
    
    def get_meta_table_columns(self):
        return {
            "created_on": '',
            "updated_on": '',
            "id": '',
        }
    
    def merge_dict(self, dict1, dict2):
        merged_dict = dict1.copy()  # create a copy of dict1
        merged_dict.update(dict2)  # update the copy with dict2
        return merged_dict
