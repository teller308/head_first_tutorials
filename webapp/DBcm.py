import psycopg2


class ConnectionError(Exception):
    pass


class UseDatabase:

    def __init__(self, config) -> None:
        self.configuration = config

    def __enter__(self) -> 'cursor':
        try:
            self.connection = psycopg2.connect(**self.configuration)
            self.cursor = self.connection.cursor()
            return self.cursor
        except psycopg2.OperationalError as err:
            raise ConnectionError(err)

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
