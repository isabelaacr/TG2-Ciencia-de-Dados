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
    

    @app.route('/somar_receitas', methods=['GET'])
    def somar_receitas():
        conn = get_db_connection()
        if conn is None:
            return jsonify({"message": "Erro na conexão com o banco de dados!"}), 500

        cursor = conn.cursor()

        try:
            cursor.execute("SELECT SUM(Preco) FROM receita")
            total = cursor.fetchone()[0]
        except mariadb.Error as e:
            return jsonify({"message": "Erro ao calcular soma das receitas!", "error": str(e)}), 500
        finally:
            cursor.close()
            conn.close()

        return jsonify({"total_precos": total})
    
    @app.route('/paciente/<int:paciente_id>/somar_receitas', methods=['GET'])
    def somar_receitas_paciente(paciente_id):
        conn = get_db_connection()
        if conn is None:
            return jsonify({"message": "Erro na conexão com o banco de dados!"}), 500

        cursor = conn.cursor()

        try:
            cursor.execute("SELECT SUM(Preco) FROM receita WHERE pacientesID = ?", (paciente_id,))
            total = cursor.fetchone()[0]
        except mariadb.Error as e:
            return jsonify({"message": "Erro ao calcular soma das receitas do paciente!", "error": str(e)}), 500
        finally:
            cursor.close()
            conn.close()

        return jsonify({"total_precos_paciente": total})

    @app.route('/consultas', methods=['GET'])
    def listar_consultas():
        conn = get_db_connection()
        if conn is None:
            return jsonify({"message": "Erro na conexão com o banco de dados!"}), 500

        cursor = conn.cursor()

        try:
            cursor.execute("""
                SELECT c.ID, c.pacientesID, p.Nome AS NomePaciente, c.medicaID, e.Nome AS NomeMedico, c.data, c.Preco
                FROM consulta c
                JOIN pacientes p ON c.pacientesID = p.ID
                JOIN empregados e ON c.medicaID = e.ID
            """)
            consultas = cursor.fetchall()
        except mariadb.Error as e:
            return jsonify({"message": "Erro ao listar consultas!", "error": str(e)}), 500
        finally:
            cursor.close()
            conn.close()

        return jsonify([
            {
                "ID": consulta[0],
                "PacienteID": consulta[1],
                "NomePaciente": consulta[2],
                "MedicoID": consulta[3],
                "NomeMedico": consulta[4],
                "Data": consulta[5],
                "Preco": consulta[6]
            }
            for consulta in consultas
        ])
    
    ### ARRUMAR ISSO /QUARTOS ou /RECEITAS ####
    @app.route('/quartos', methods=['GET'])
    def listar_quartos():
        conn = get_db_connection()
        if conn is None:
            return jsonify({"message": "Erro na conexão com o banco de dados!"}), 500

        cursor = conn.cursor()

        try:
            cursor.execute("""
                SELECT q.ID, q.numero, q.consultorioID, 
                   (SELECT COUNT(*) FROM pacientes p WHERE p.quartosID = q.ID) AS lotacao, 
                   (SELECT GROUP_CONCAT(e.Nome SEPARATOR ', ') FROM lotacao l 
                    JOIN enfermeira en ON l.enfermeiraID = en.EmpregadosID 
                    JOIN empregados e ON en.EmpregadosID = e.ID 
                    WHERE l.quartosID = q.ID) AS enfermeiraResponsavel
                FROM quartos q
            """)
            quartos = cursor.fetchall()
        except mariadb.Error as e:
            return jsonify({"message": "Erro ao listar quartos!", "error": str(e)}), 500
        finally:
            cursor.close()
            conn.close()

        return jsonify([
            {
            "id": quarto[0],  # Inteiro
            "numero": quarto[1],  # Inteiro
            "idConsultorio": quarto[2] if quarto[2] else None,  # Inteiro ou None
            "lotacao": quarto[3],  # Inteiro
            "enfermeiraResponsavel": str(quarto[4] or "")  # Sempre string
            }
            for quarto in quartos
        ])

    @app.route('/inserir_funcionario', methods=['POST'])
    def add_empregado():
        data = request.get_json()
        required_fields = ['ID', 'Nome', 'CPF', 'Tipo']

        if not all(field in data for field in required_fields):
            return jsonify({"message": "Faltam dados de entrada!"}), 400

        success = insert_empregado(data)
        if not success:
            return jsonify({"message": "Erro ao inserir empregado!"}), 500

        return jsonify({"message": "Empregado inserido com sucesso!"}), 201
