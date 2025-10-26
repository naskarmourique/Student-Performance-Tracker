import os
from flask import Flask, render_template, request, redirect, url_for, flash, session, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "default_secret")

# Database setup (PostgreSQL or fallback)
db_uri = os.getenv("DATABASE_URL", "sqlite:///students.db")
if db_uri.startswith("postgres://"):
    db_uri = db_uri.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"

# ---------------- MODELS ----------------

class Teacher(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll_number = db.Column(db.String(50), unique=True, nullable=False)
    grades = db.relationship("Grade", backref="student", lazy=True)

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50), nullable=False)
    marks = db.Column(db.Float, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)

# ---------------- LOGIN ----------------

@login_manager.user_loader
def load_user(user_id):
    return Teacher.query.get(int(user_id))

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("Database tables created.")

@app.cli.command("create-user")
def create_user():
    username = os.getenv("DEFAULT_TEACHER_USERNAME", "Mourique")
    password = os.getenv("DEFAULT_TEACHER_PASSWORD", "izya")
    if Teacher.query.filter_by(username=username).first():
        print("User already exists.")
    else:
        hashed = generate_password_hash(password)
        new_user = Teacher(username=username, password_hash=hashed)
        db.session.add(new_user)
        db.session.commit()
        print(f"Created user {username}")

# ---------------- ROUTES ----------------

@app.route("/")
@login_required
def home():
    students = Student.query.all()
    return render_template("index.html", students=students)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = Teacher.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for("home"))
        flash("Invalid credentials")
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/add_student", methods=["POST"])
@login_required
def add_student():
    name = request.form["name"]
    roll = request.form["roll_number"]
    if Student.query.filter_by(roll_number=roll).first():
        flash("Roll number already exists!")
    else:
        db.session.add(Student(name=name, roll_number=roll))
        db.session.commit()
        flash("Student added successfully!")
    return redirect(url_for("home"))

@app.route("/student/<int:id>")
@login_required
def student_details(id):
    student = Student.query.get_or_404(id)
    grades = {g.subject: g.marks for g in student.grades}
    avg = sum(grades.values()) / len(grades) if grades else 0
    return render_template("student_details.html", student=student, grades=grades, avg=avg)

@app.route("/add_grade/<int:id>", methods=["POST"])
@login_required
def add_grade(id):
    student = Student.query.get_or_404(id)
    subject = request.form["subject"]
    marks = float(request.form["marks"])
    if 0 <= marks <= 100:
        db.session.add(Grade(subject=subject, marks=marks, student=student))
        db.session.commit()
        flash("Grade added!")
    else:
        flash("Marks must be between 0 and 100")
    return redirect(url_for("student_details", id=id))

@app.route("/edit_student/<int:id>", methods=["GET", "POST"])
@login_required
def edit_student(id):
    student = Student.query.get_or_404(id)
    if request.method == "POST":
        student.name = request.form["name"]
        student.roll_number = request.form["roll_number"]
        db.session.commit()
        flash("Student details updated successfully!")
        return redirect(url_for("home"))
    return render_template("edit_student.html", student=student)

@app.route("/delete_student/<int:id>", methods=["POST"])
@login_required
def delete_student(id):
    student = Student.query.get_or_404(id)
    for grade in student.grades:
        db.session.delete(grade)
    db.session.delete(student)
    db.session.commit()
    flash("Student deleted successfully!")
    return redirect(url_for("home"))

@app.route("/edit_grade/<int:id>", methods=["GET", "POST"])
@login_required
def edit_grade(id):
    grade = Grade.query.get_or_404(id)
    if request.method == "POST":
        grade.subject = request.form["subject"]
        grade.marks = float(request.form["marks"])
        if 0 <= grade.marks <= 100:
            db.session.commit()
            flash("Grade updated successfully!")
            return redirect(url_for("student_details", id=grade.student_id))
        else:
            flash("Marks must be between 0 and 100")
    return render_template("edit_grade.html", grade=grade)

@app.route("/delete_grade/<int:id>", methods=["POST"])
@login_required
def delete_grade(id):
    grade = Grade.query.get_or_404(id)
    student_id = grade.student_id
    db.session.delete(grade)
    db.session.commit()
    flash("Grade deleted successfully!")
    return redirect(url_for("student_details", id=student_id))

@app.route("/stats", methods=["GET"])
@login_required
def stats():
    subject = request.args.get("subject")
    topper = None
    class_avg = None
    if subject:
        grades = Grade.query.filter_by(subject=subject).all()
        if grades:
            topper_grade = max(grades, key=lambda g: g.marks)
            topper = topper_grade.student
            class_avg = sum(g.marks for g in grades) / len(grades)
    return render_template("stats.html", subject=subject, topper=topper, class_avg=class_avg)

@app.route("/backup")
@login_required
def backup():
    students = Student.query.all()
    backup_content = ""
    for student in students:
        backup_content += f"Name: {student.name}\n"
        backup_content += f"Roll Number: {student.roll_number}\n"
        backup_content += "Grades:\n"
        for grade in student.grades:
            backup_content += f"  {grade.subject}: {grade.marks}\n"
        backup_content += "---\n"

    response = make_response(backup_content)
    response.headers.set("Content-Type", "text/plain")
    response.headers.set("Content-Disposition", "attachment; filename=students_backup.txt")
    return response

if __name__ == "__main__":
    app.run(debug=True)