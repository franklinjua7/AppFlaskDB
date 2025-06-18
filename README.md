# AppFlaskDB

Ejemplo de una aplicación en Flask, en la cual nos vamos a conectar a una base de datos .SQLITE y una base de datos de .MYSQL.

Para ello vamos a trabajar el proyecto en modulos, y para ello vamos a utilizar el Blueprint.

## Migración

Vamos a realizar cambios en las clases de los modelos de las tablas de la base de datos.
Existen dos métodos para realizar ello:

01. Primer Método: Vamos a actualizar las tablas mediante comando y para ello vamos a ejecutar los siguientes comandos:
* ESTILO MÁS MODERNO

```sh
(venv) [root@DESKTOP-0JKCAMP AppFlaskDB]$ flask --app app_mysql db init ## Comando para iniciarlizar el FOLDER de migraciones
(venv) [root@DESKTOP-0JKCAMP AppFlaskDB]$ flask --app app_mysql db migrate -m "Descripción de la migración"
(venv) [root@DESKTOP-0JKCAMP AppFlaskDB]$ flask --app app_mysql db stamp ## Si es que la base de datos ya se encuentra creada, sino "upgrade"
(venv) [root@DESKTOP-0JKCAMP AppFlaskDB]$ flask --app app_mysql db upgrade
```

02. Utilizando un archivo denominado "manage.py", y lo vamos a hacer de la siguiente manera:

Creamos el archivo: manage.py

```python
# manage.py
from flask.cli import FlaskGroup
from app_mysql import app, db

cli = FlaskGroup(app)

if __name__=='__main__':
    cli()
```

Entonces, procedemos a ejecutar los siguientes comandos:

```sh
python manage.py db init
python manage.py db migrate -m "Comentario"
python manage.py db upgrade
```