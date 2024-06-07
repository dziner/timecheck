from app import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    clock_in_time = db.Column(db.DateTime, nullable=True)
    clock_out_time = db.Column(db.DateTime, nullable=True)
