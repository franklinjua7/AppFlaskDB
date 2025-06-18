# connections/mysql/models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

# Instancia de la CLASE de BD
db = SQLAlchemy()

# Declaramos la CLASE de STUDENT
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    dni = db.Column(db.String(8), nullable=False)
    grade = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    bio = db.Column(db.Text)

    def __repr__(self):
        return f'Student {self.firstname}'


class Teacher(db.Model):
    __tablename__='teachers'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'Teacher {self.firstname}'