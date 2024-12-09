import mariadb

# Handles the connection to the mariadb
# This should be imported in models.py and views.py
def get_db_connection():
    try:
        conn = mariadb.connect(
            host='localhost',
            user='root',
            password='root',
            database='simpleclinic'
        )
        return conn
    except mariadb.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None