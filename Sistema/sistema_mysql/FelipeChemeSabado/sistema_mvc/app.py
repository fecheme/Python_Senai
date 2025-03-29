
from flask import Flask
from flask_cors import CORS
CORS
from flask_mysqldb import MySQL # biblioteca mysql flask
from controllers.produto_controller import produto_bp
import config

app = Flask(__name__) # Instanciar variaveis
app.config.from_object(config) # Confingurando Variaveis
 

mysql =  MySQL(app)

# passa a conexao para os controllers
app.mysql = mysql

# registrar o controller 
app.register_blueprint(produto_bp)

# rodar o app
if __name__ == '__main__':
    app.run(debug=True)
                                           