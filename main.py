from flask import Flask, request, jsonify, render_template
import mariadb  # Usando o conector mariadb
app = Flask(__name__, template_folder='./templates')
@app.route('/') 
def home(): 
    return render_template('index.html')
                                            
# Função para obter a conexão com o MariaDB
def get_db_connection():
    try:
        # Conectando ao MariaDB
        conn = mariadb.connect(
            host='localhost',       # Endereço do servidor
            user='root',            # Usuário do banco
            password='sua_senha',   # Senha do banco
            database='simpleclinic'  # Nome do banco de dados
        )
        return conn
    except mariadb.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
       
# rota para obter todos os pacientes
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
    return jsonify(pacientes)
   
# Rota para inserir um paciente
@app.route('/inserir_paciente', methods=['POST'])
def insert_paciente():
    data = request.get_json()
    conn = get_db_connection()
    if conn is None:
        return jsonify({"message": "Erro na conexão com o banco de dados!"}), 500
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pacientes (ID, Nome, Cpf, Restricoes, quartosID) VALUES  (%s, %s, %s, %s, %s)",
                   (data['ID'], data['Nome'], data['Cpf'], data['Restricoes'], data['quartosID']))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "Paciente inserido com sucesso!"}), 201
if __name__ == "__main__":
    app.run(debug=True, port=5000)
