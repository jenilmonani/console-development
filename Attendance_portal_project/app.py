from flask import Flask, render_template, redirect, url_for, request
from models import db, Student, Course, Attendance, Teacher# it is user defined module 
from datetime import date
# flask is framework which is uses to handle get and post htttp_request and generates the url
#in cmd and integrates database using sqlalchemy extension and handle connections of database.

app = Flask(__name__)# start the flask application or flask app setup.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'# it is used to connect with
#database and store data in attendance.db file.

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'#it is for security purpose

db.init_app(app)# links the app with database using sqlalchemy

# Initialize the database tables (only required the first time)
with app.app_context():
    db.create_all() #creates the database tables

@app.route('/')#defines the route (URL) for a specific webpage or view function.
# / means homepage displays the home page
def index():
    return render_template('index.html')#render_template() function is used to load the html
#file from templates folder

# Register a student
@app.route('/register', methods=['GET', 'POST'])# get method loads the form to fill and post
#method submits the form to database
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        student = Student(name=name, email=email)
        db.session.add(student)#add to database
        db.session.commit()#save in database
        return redirect(url_for('index'))#return to home page
    return render_template('register.html')

# Register a teacher
@app.route('/register_teacher', methods=['GET', 'POST'])# similar to  the register student
def register_teacher():
    if request.method == 'POST': #if user submits the form this if will executed.
        name = request.form['name']
        email = request.form['email']
        teacher = Teacher(name=name, email=email)
        db.session.add(teacher)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register_teacher.html')# else register page will open to fill.

# Register a course
@app.route('/register_course', methods=['GET', 'POST'])
def register_course():
    if request.method == 'POST':
        course_name = request.form['course_name']
        course = Course(course_name=course_name)
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register_course.html')

# Mark attendance
@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    #Retrieves all students and courses from the database to
    #show in the attendance form.
    students = Student.query.all()
    courses = Course.query.all()
    if request.method == 'POST':
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        status = request.form['status']
        attendance = Attendance(student_id=student_id, course_id=course_id, status=status, date=date.today())
        db.session.add(attendance)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('attendance.html', students=students, courses=courses)

# View students
@app.route('/view_students')
def view_students():
    students = Student.query.all()#shows all student 
    return render_template('view_students.html', students=students)

# View teachers
@app.route('/view_teachers')
def view_teachers():
    teachers = Teacher.query.all()#shows all teacher
    return render_template('view_teachers.html', teachers=teachers)

# View courses
@app.route('/view_courses')
def view_courses():
    courses = Course.query.all()#shows all course
    return render_template('view_courses.html', courses=courses)

# View attendance records
@app.route('/view_attendance')
def view_attendance():
    attendance_records = Attendance.query.all()#shows all attendance
    return render_template('view_attendance.html', attendance_records=attendance_records)

if __name__ == "__main__": #It checks if script is direct running then it will enter in block
    # else if script is imported from another file.
    app.run(debug=True) # runs the app in debug mode and if some errors come then it displays message
