from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='./templates')
    
    from views import init_routes
    init_routes(app) 

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5050)
