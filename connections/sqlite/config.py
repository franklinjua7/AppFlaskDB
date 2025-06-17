# connections/sqlite/config.py
import os
basedir = os.path.abspath(os.path.dirname(__file__))

conexion_config = 'sqlite:///' + os.path.join(basedir, 'database.db') 