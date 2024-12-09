#onde configuro as tabelas do banco de dados models.py

import mariadb
from db import get_db_connection

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
    
    return [
        {
            "ID": paciente[0],
            "Nome": paciente[1],
            "Cpf": paciente[2],
            "Restricoes": paciente[3],
            "quartosID": paciente[4]
        }
        for paciente in pacientes
    ]

def insert_paciente(data):
    conn = get_db_connection()
    if conn is None:
        return False
    
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO pacientes (ID, Nome, Cpf, Restricoes, quartosID) VALUES (%s, %s, %s, %s, %s)",
        (data['ID'], data['Nome'], data['Cpf'], data['Restricoes'], data['quartosID'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return True
