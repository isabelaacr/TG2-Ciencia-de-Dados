from flask import Flask, render_template, jsonify, request
import mariadb

app = Flask(__name__)

# Função para obter a conexão com o MariaDB
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

# Rota para renderizar a homepage
@app.route('/')
def homepage():
    return render_template('index.html')  

# Consultar pacientes no banco de dados
@app.route('/pacientes', methods=['GET'])
def get_pacientes():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"message": "Erro na conexão com o banco de dados!"}), 500
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pacientes")
    pacientes = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # Retorna os pacientes como JSON 
    return jsonify(pacientes)

# Inserir um novo paciente
@app.route('/paciente', methods=['POST'])
def insert_paciente():
    data = request.get_json()
    conn = get_db_connection()
    if conn is None:
        return jsonify({"message": "Erro na conexão com o banco de dados!"}), 500
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pacientes (ID, Nome, Cpf, Restricoes, quartosID) VALUES (?, ?, ?, ?, ?)",
                   (data['ID'], data['Nome'], data['Cpf'], data['Restricoes'], data['quartosID']))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "Paciente inserido com sucesso!"}), 201

# @app.route('/paciente', methods=['PATCH'])
# def insert_paciente():
#     data = request.get_json()
#     conn = get_db_connection()
#     if conn is None:
#         return jsonify({"message": "Erro na conexão com o banco de dados!"}), 500
    
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO pacientes (ID, Nome, Cpf, Restricoes, quartosID) VALUES (?, ?, ?, ?, ?)",
#                    (data['ID'], data['Nome'], data['Cpf'], data['Restricoes'], data['quartosID']))
#     conn.commit()
#     cursor.close()
#     conn.close()
    
#     return jsonify({"message": "Paciente inserido com sucesso!"}), 201