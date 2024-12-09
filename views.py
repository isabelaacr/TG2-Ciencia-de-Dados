from flask import render_template, request, jsonify
from models import *
from db import get_db_connection
import mariadb

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

        data = request.get_json()
        required_fields = ['ID', 'Nome', 'Cpf', 'Restricoes', 'quartosID']
        
        # Validar os dados de entrada
        if not all(field in data for field in required_fields):
            return jsonify({"message": "Faltam dados de entrada!"}), 400
        
        success = insert_paciente(data)
        if not success:
            return jsonify({"message": "Erro ao inserir paciente!"}), 500
        return jsonify({"message": "Paciente inserido com sucesso!"}), 201

    @app.route('/count_pacientes', methods=['GET'])
    def count_pacientes():

        count = get_count_pacientes()

        if count is None:
            return jsonify({"message" : "Erro ao contar todos os pacientes."}), 500
        
        return jsonify({"total_pacientes": count})

    @app.route('/count_pacientes_por_quarto', methods=['GET'])
    def pacientes_por_quarto():
        
        dados = get_count_pacientes_por_quarto()

        if dados is None:
            return jsonify({"message" : "Erro ao contar pacientes por quarto."}), 500
        
        return jsonify(dados)

    @app.route('/consultorios', methods=['GET'])
    def consultorios():

        consultorios_list = get_consultorios()

        if consultorios_list is None:
            return jsonify({"message": "Erro na conexão com o banco de dados!"}), 500
        
        return jsonify(consultorios_list)
    
    @app.route('/receitas', methods=['GET'])
    def get_receitas():
    
        receitas = get_all_receitas()

        if receitas is None:
            return jsonify({"message" : "Erro ao buscar todas as receitas."}),500
    
        return jsonify(receitas)
    
    
    @app.route('/empregados', methods=['GET'])
    def get_empregados():
    
        empregados = get_all_empregados()
        
        if empregados is None:
            return jsonify({"message": "Erro ao buscar todos os empregados!"}), 500
        
        return jsonify(empregados)