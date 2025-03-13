from flask_sqlalchemy import SQLAlchemy # it is module.
#This is the object that connects your Flask app to the database
db = SQLAlchemy()#it is used to create database. automatic table creation.

class Student(db.Model): #defines a student class. table in database.
    id = db.Column(db.Integer, primary_key=True) #defining a column 
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Course(db.Model): # defines a course class. table in database
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)

class Attendance(db.Model): # defines a attendance class. table in database
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(10), nullable=False)

    student = db.relationship('Student', backref=db.backref('attendances', lazy=True))
    course = db.relationship('Course', backref=db.backref('attendances', lazy=True))
''' this creates the relationships between two table.  backref will reverse connect the tables so
all data can fetch easily from both table and lazy is for only that records which are matching using condition'''
class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
