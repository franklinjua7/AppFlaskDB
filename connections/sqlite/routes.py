# connections/sqlite/routes.py
from flask import Blueprint, render_template, request, redirect, url_for
from connections.sqlite.models import Student, db

bp_sqlite = Blueprint('sqlite_routes', __name__)

@bp_sqlite.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', route_prefix='sqlite_routes', students=students)


@bp_sqlite.route('/<int:student_id>/')
def student(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template('student.html', route_prefix='sqlite_routes', student=student)


@bp_sqlite.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = request.form['bio']
        student = Student(firstname=firstname,
                          lastname=lastname,
                          email=email,
                          age=age,
                          bio=bio)
        db.session.add(student)
        db.session.commit()

        return redirect(url_for('sqlite_routes.index', route_prefix='sqlite_routes'))

    return render_template('create.html', route_prefix='sqlite_routes')


@bp_sqlite.route('/<int:student_id>/edit/', methods=('GET', 'POST'))
def edit(student_id):
    student = Student.query.get_or_404(student_id)

    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        age = int(request.form['age'])
        bio = request.form['bio']

        student.firstname = firstname
        student.lastname = lastname
        student.email = email
        student.age = age
        student.bio = bio

        db.session.add(student)
        db.session.commit()

        return redirect(url_for('sqlite_routes.index', route_prefix='sqlite_routes'))

    return render_template('edit.html', route_prefix='sqlite_routes', student=student)


@bp_sqlite.post('/<int:student_id>/delete/')
def delete(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('sqlite_routes.index', route_prefix='sqlite_routes'))