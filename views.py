from flask import render_template, request, jsonify
import mariadb

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
    def add_paciente():
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

    @app.route('/count_pacientes', methods=['GET'])
    def count_pacientes():
        conn = get_db_connection()  
        if conn is None:
            return jsonify({"message": "Erro na conexão com o banco de dados!"}), 500
        
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM pacientes") 
        count = cursor.fetchone()[0]  
        cursor.close()
        conn.close()
        
        return jsonify({
            "total_pacientes": count  
        })

    @app.route('/count_pacientes_por_quarto', methods=['GET'])
    def count_pacientes_por_quarto():
        conn = get_db_connection()
        if conn is None:
            return jsonify({"message": "Erro na conexão com o banco de dados!"}), 500
        
        cursor = conn.cursor()
        cursor.execute("""
            SELECT quartosID, COUNT(*) 
            FROM pacientes 
            GROUP BY quartosID
        """)
        dados = cursor.fetchall()
        cursor.close()
        conn.close()

        lista_dados = [{"quartoID": dado[0], "total_pacientes": dado[1]} for dado in dados]
        return jsonify(lista_dados)


    @app.route('/consultorios', methods=['GET'])
    def get_consultorios():
    
        conn = get_db_connection()
        if conn is None:
            return jsonify({"message": "Erro na conexão com o banco de dados!"}), 500
    
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM consultorio")
        consultorios = cursor.fetchall()
        cursor.close()
        conn.close()

        consultorios_list = [
            { "ID"   : consultorio[0],
              "CNPJ" : consultorio[1]}
            for consultorio in consultorios]
    
        return jsonify(consultorios_list)
    
 

    @app.route('/receitas', methods=['GET'])
    def get_receitas():
    
        conn = get_db_connection()
        if conn is None:
            return jsonify({"message": "Erro na conexão com o banco de dados!"}), 500
    
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM receita")
        receitas = cursor.fetchall()
        cursor.close()
        conn.close()

        receitas_list = [
            { "receitaID"   : receitas[0],
              "medicamento" : receitas[1]}
            for receita in receitas]
    
        return jsonify(receitas_list)
    
    
    @app.route('/empregados', methods=['GET'])
    def get_empregados():
    
        conn = get_db_connection()
        if conn is None:
            return jsonify({"message": "Erro na conexão com o banco de dados!"}), 500
    
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM empregados")
        empregados = cursor.fetchall()
        cursor.close()
        conn.close()

        empregados_list = [
            { "empregadoID" : empregado[0],
              "nome"        : empregado[1],
              "CPF"         : empregado[2],
              "tipo"        : empregado[3]}
            for empregado in empregados]
    
        return jsonify(empregados_list)