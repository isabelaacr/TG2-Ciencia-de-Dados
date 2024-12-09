from flask import render_template, request, jsonify
import mariadb
from models import get_all_pacientes, insert_paciente
from db import get_db_connection

def init_routes(app):
    @app.route('/') 
    def home(): 
        return render_template('index.html')

    @app.route('/pacientes', methods=['GET'])
    def get_pacientes():

        pacientes = get_all_pacientes()

        if pacientes is None:
            return jsonify({"message": "Erro ao buscar pacientes!"}), 500
                
        return jsonify(pacientes)

    @app.route('/inserir_paciente', methods=['POST'])
    def add_paciente():
        data = request.get_json()
        required_fields = ['ID', 'Nome', 'Cpf', 'Restricoes', 'quartosID']
        
        # Validar os dados de entrada
        if not all(field in data for field in required_fields):
            return jsonify({"message": "Faltam dados de entrada!"}), 400
        
        success = insert_paciente(data)
        if not success:
            return jsonify({"message": "Erro ao inserir paciente!"}), 500
        return jsonify({"message": "Paciente inserido com sucesso!"}), 201
    
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