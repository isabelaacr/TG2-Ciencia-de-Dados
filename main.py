from flask import Flask, request, jsonify, render_template
import mariadb  # Usando o conector mariadb

app = Flask(__name__, template_folder='./templates')
   
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

if __name__ == "__main__":
    app.run(debug=True, port=5000)
