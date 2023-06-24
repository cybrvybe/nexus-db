
import requests
import os
from urllib.parse import urljoin
from util_scripts.logs.log_handler import LogHandler

class DbDirectAccessPoint:
    def __init__(self, nexus_db_api_url = os.getenv("DB_API_URL", "http://127.0.0.1:5000")):
        self.nexus_db_api_url = nexus_db_api_url
        self.logger = LogHandler()

    def _construct_url(self, end_slugs):
        return urljoin(self.nexus_db_api_url, end_slugs)

    def create_db(self, db_name: str):
        response = self._post_request("/database/create", {"db_name": db_name})
        self.logger.log_info(f"{db_name} database creation response: {response.json()}")
        return response.json()

    def create_schema(self, schema_name: str):
        self._post_request("/schema/create", {"schema_name": schema_name})

    def create_and_log_table(self, schema_name: str, table_name: str, table_columns: dict):
        table_columns = {**self._get_default_table_columns(), **table_columns}
        payload = {"schema_name": schema_name, "table_name": table_name, "table_columns": table_columns}
        response = self._post_request("/table/create", payload)
        self.logger.log_info(f"Table {schema_name}.{table_name} creation response: {response.json()}")
        return response.json()

    def create_tables(self, schema_name: str, tables: list):
        for table in tables:
            self.create_and_log_table(schema_name, **table)
        self.logger.log_success(f"{schema_name} tables created successfully.")

    def _get_default_table_columns(self):
        return {"created_on": '', "updated_on": '', "id": '',}

    def _post_request(self, end_slug: str, payload: dict):
        try:
            response = requests.post(self._construct_url(end_slug), json=payload)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as err:
            self.logger.log_error(f"HTTP error occurred: {err}")
            raise SystemExit(err)
        except Exception as err:
            self.logger.log_error(f"Error occurred: {err}")
            raise SystemExit(err)
