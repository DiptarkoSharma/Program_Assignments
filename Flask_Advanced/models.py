from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    pin = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<Student {self.name}>'
