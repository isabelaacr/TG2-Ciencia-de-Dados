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

def get_count_pacientes():
    conn = get_db_connection()

    if conn is None:
        return None
    
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM pacientes") 
    count = cursor.fetchone()[0]  
    cursor.close()
    conn.close()

    return count

def get_count_pacientes_por_quarto():

    conn = get_db_connection()

    if conn is None:
        return None
    
    cursor = conn.cursor()
    cursor.execute("""
        SELECT quartosID, COUNT(*) 
        FROM pacientes 
        GROUP BY quartosID
    """)

    dados= cursor.fetchall()
    cursor.close()
    conn.close()

    return [{"quartoID": dado[0], "total_pacientes": dado[1]} for dado in dados]
    
def get_consultorios():
    
    conn = get_db_connection()

    if conn is None:
        return None
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM consultorio")
    consultorios = cursor.fetchall()
    cursor.close()
    conn.close()

    return [
        {
            "ID"   : consultorio[0],
            "CNPJ" : consultorio[1]
        } for consultorio in consultorios
    ]

def get_all_receitas():

    conn = get_db_connection()

    if conn is None:
        return None
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM receita")

    receitas = cursor.fetchall()
    cursor.close()
    conn.close()

    return [
        {
            "receitaID" : receitas[0],
            "medicamento" : receitas[1]
        } for receita in receitas
    ]

def get_all_empregados():

    conn = get_db_connection()

    if conn is None:
        return None

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM empregados")

    empregados = cursor.fetchall()
    cursor.close()
    conn.close()

    return [
        {
            "empregadoID" : empregado[0],
            "nome"        : empregado[1],
            "CPF"         : empregado[2],
            "tipo"        : empregado[3]
        } for empregado in empregados
    ]