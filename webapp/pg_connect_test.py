import psycopg2


dbconfig = {
    'host': '127.0.0.1',
    'user': 'postgres',
    'password': '***',
    'database': 'vsearchlogdb',
    'port': '5432',
}

connection = ''

try:
    connection = psycopg2.connect(**dbconfig)
    cursor = connection.cursor()

    _SQL = """select version();"""
    cursor.execute(_SQL)

    record = cursor.fetchall()
    for row in record:
        print(record)

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to postgresql. ", error)
finally:
    if(connection):
        cursor.close()
        connection.commit()
        connection.close()
        print("PostgreSQL connection closed")