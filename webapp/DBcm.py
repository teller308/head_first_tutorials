import psycopg2


class UseDatabase:

    def __init__(self, config) -> None:
        self.configuration = config

    def __enter__(self) -> 'psycopg2.connect.cursor':
        self.connection = psycopg2.connect(**self.configuration)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
