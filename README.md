# NexusDB

NexusDB is a hybrid CLI tool that interfaces with both a PostgreSQL and a Vector Database. It provides a user-friendly and intuitive command line interface for regular database operations while also offering advanced features for AI-related queries involving similarity searches in high-dimensional data.

## Getting Started

1. Clone this repository:

    ```
    git clone https://github.com/cybrvybe/nexus_db.git
    cd nexus_db
    ```

2. Install the dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Build the Docker image:

    ```
    docker build -t nexus_db .
    ```

4. Run the Docker container:

    ```
    docker run -p 80:80 nexus_db
    ```

5. You should now be able to access the NexusDB CLI on `localhost:80`.

## CLI Commands

- `help`: Display the list of available commands and their usage.
- `init`: Initialize the databases and the CLI tool.
- `create`: Create a new table in the database.
- `insert`: Insert a row of data into a specified table.
- `update`: Update data in a specified table.
- `delete`: Delete data from a specified table.
- `query`: Query data from the database using SQL.
- `vecquery`: Query data from the vector database using a similarity search.

## Development Guide

1. Clone the repository and install the dependencies.
2. Use Docker to run the PostgreSQL and Vector Databases locally.
3. Run the CLI tool and execute the 'init' command to initialize the databases.
4. Use the 'help' command to learn about the available commands and how to use them.
5. Start developing and testing new features.

## License

This project is licensed under the terms of the MIT license.
