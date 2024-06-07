from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # 로컬 SQLite DB 사용
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    clock_in_time = db.Column(db.DateTime, nullable=True)
    clock_out_time = db.Column(db.DateTime, nullable=True)

@app.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

@app.route('/clock_in', methods=['POST'])
def clock_in():
    employee_id = request.form['employee_id']
    employee = Employee.query.get(employee_id)
    employee.clock_in_time = datetime.now()
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/clock_out', methods=['POST'])
def clock_out():
    employee_id = request.form['employee_id']
    employee = Employee.query.get(employee_id)
    employee.clock_out_time = datetime.now()
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
