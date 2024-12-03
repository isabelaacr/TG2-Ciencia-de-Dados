from flask import render_template, request, jsonify
import mariadb

# Function to get DB connection
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

def init_routes(app):
    @app.route('/') 
    def home(): 
        return render_template('index.html')

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
        
        pacientes_list = []
        for paciente in pacientes:
            pacientes_list.append({
                "ID": paciente[0],
                "Nome": paciente[1],
                "Cpf": paciente[2],
                "Restricoes": paciente[3],
                "quartosID": paciente[4]
            })
        
        return jsonify(pacientes_list)

    @app.route('/inserir_paciente', methods=['POST'])
    def insert_paciente():
        data = request.get_json()

        if not all(key in data for key in ['ID', 'Nome', 'Cpf', 'Restricoes', 'quartosID']):
            return jsonify({"message": "Falta dados de entrada!"}), 400
        
        conn = get_db_connection()
        if conn is None:
            return jsonify({"message": "Erro na conexão com o banco de dados!"}), 500
        
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pacientes (ID, Nome, Cpf, Restricoes, quartosID) VALUES (%s, %s, %s, %s, %s)",
                       (data['ID'], data['Nome'], data['Cpf'], data['Restricoes'], data['quartosID']))
        conn.commit()
        cursor.close()
        conn.close()
        
        return jsonify({"message": "Paciente inserido com sucesso!"}), 201
