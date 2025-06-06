from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)



class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    officername = db.Column(db.String(60), nullable=False)
    day = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    campus = db.Column(db.String(60), nullable=False)
    excelfile = db.Column(db.String(120), nullable=False)
    exceldata = db.relationship('ExcelData', backref='report', lazy=True,cascade='all, delete-orphan')  

    def __init__(self, officername, day, month, year, campus, excelfile):
        self.officername = officername
        self.day = day
        self.month = month
        self.year = year
        self.campus = campus
        self.excelfile = excelfile

    def get_json(self):
        return {
            'id': self.id,
            'officername': self.officername,
            'day': self.day,
            'month': self.month,
            'year': self.year,
            'campus': self.campus,
            'excelfile': self.excelfile
        }


class ExcelData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(60), nullable=False)
    students = db.Column(db.Integer, nullable=False)
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'), nullable=False)

    def __init__(self, department, students, report_id):
        self.department = department
        self.students = students
        self.report_id = report_id

    def get_json(self):
        return {
            'id': self.id,
            'department': self.department,
            'students': self.students,
            'report_id': self.report_id
        }