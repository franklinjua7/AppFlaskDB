# app.py
from flask import Flask
from connections.sqlite.routes import bp_sqlite
from connections.sqlite.models import db
from connections.sqlite.config import conexion_config

# Inicializamos la INSTANCIA de Flask
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='mysql://franklinjuarez:franklinjuarez@127.0.0.1:3306/colegio' 
app.config['SQLALCHEMY_DATABASE_URI']= conexion_config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Registramos las rutas desde el BLUEPRINT
app.register_blueprint(bp_sqlite)

# Inicializamos la INSTANCIA de la BD
db.init_app(app)
with app.app_context():
    db.create_all()

if __name__=='__main__':
    app.run(host='0.0.0.0', port='7777', debug=True)