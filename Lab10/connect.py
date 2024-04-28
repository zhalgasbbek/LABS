import psycopg2
from config import load_config

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    config = load_config()
    connect(config)
    conn = psycopg2.connect("dbname=suppliers user=postgres password=adal host=localhost por=5433")
    
    
#В-третьих, создайте новый файл с именем, который использует модуль для чтения конфигурации и подключения к PostgreSQL:connect.pyconfig.py