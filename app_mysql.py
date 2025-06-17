# app_mysql.py
from flask import Flask
from connections.mysql.config import conexion_config
from connections.mysql.routes import bp_mysql
from connections.mysql.models import db

# Inicializamos la INSTANCIA de FLASK
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = conexion_config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Registramos las RUTAS desde el BLUEPRINT
app.register_blueprint(bp_mysql)

# Registramos la INSTANCIA de la BD
db.init_app(app)
with app.app_context():
    db.create_all()

if __name__=='__main__':
    app.run(host='0.0.0.0', port='7778', debug=True)