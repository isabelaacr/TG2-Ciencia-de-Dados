#onde configuro as tabelas do banco de dados models.py

import mariadb

# Função para obter a conexão com o banco de dados
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

# Função para buscar todos os pacientes
def get_all_pacientes():
    conn = get_db_connection()
    if conn is None:
        return None
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pacientes")
    pacientes = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return pacientes

def insert_paciente(data):
    conn = get_db_connection()
    if conn is None:
        return False
    
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO pacientes (ID, Nome, Cpf, Restricoes, quartosID) VALUES (?, ?, ?, ?, ?)",
        (data['ID'], data['Nome'], data['Cpf'], data['Restricoes'], data['quartosID'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return True
