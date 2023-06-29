from flask import Flask, request, jsonify
from .postgres.db_connection import DbConnection

from .postgres.db_manager import DbManager
from ...core.api import utils

app = Flask(__name__)

db_connection = DbConnection(
    user="postgres",
    password="n0b0dy",
    host="172.17.0.3",
    port=5432
)
db_manager = DbManager(db_connection)

@app.route('/database/create', methods=['POST'])
def create_database():
    db_name = request.json.get('db_name')
    db_manager.create_db(db_name)
    return jsonify({'message': f'Database {db_name} created successfully'}), 201

@app.route('/database/delete', methods=['DELETE'])
def delete_database():
    db_name = request.json.get('db_name')
    db_manager.delete_db(db_name)
    return jsonify({'message': f'Database {db_name} deleted successfully'}), 200

@app.route('/schema/create', methods=['POST'])
def create_schema():
    schema_name = request.json.get('schema_name')
    schema_manager = utils.get_schema_manager(request, db_connection)
    schema_manager.create_schema(schema_name)
    return jsonify({'message': f'Schema {schema_name} created successfully'}), 201

@app.route('/schema/delete', methods=['DELETE'])
def delete_schema():
    schema_name = request.json.get('schema_name')
    schema_manager = utils.get_schema_manager(request, db_connection)
    schema_manager.delete_schema(schema_name)
    return jsonify({'message': f'Schema {schema_name} deleted successfully'}), 200

@app.route('/table/create', methods=['POST'])
def create_table():
    table_manager = utils.get_table_manager(request, db_connection)
    table_name = request.json.get('table_name')
    columns = request.json.get('columns')
    table_manager.create_table(table_name, columns)
    return jsonify({'message': f'Table {table_name} created successfully'}), 201

@app.route('/table/delete', methods=['DELETE'])
def delete_table():
    table_manager = utils.get_table_manager(request, db_connection)
    table_name = request.json.get('table_name')
    table_manager.delete_table(table_name)
    return jsonify({'message': f'Table {table_name} deleted successfully'}), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)
