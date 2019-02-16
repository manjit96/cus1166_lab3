from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

course1 = ('Logical Design', 72694)
course2 = ('Theory of Programming Languages', 73041)
course3 = ('Finite Automata & Formal Languages', 75303)
course4 = ('Linear Algebra', 75309)
course5 = ('Principles of Economics II', 72161 )
course6 = ('Positive Psychology', 73907)
classes = [course1, course2, course3, course4, course5, course6]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", classes=classes)


@app.route("/layout")
def layout():
    return render_template("layout.html")


@app.route("/add_course")
def add_course():
    return render_template("index.html")


@app.route("/register_student/<int:course_id>", methods=['POST'])
def register_student():
    return render_template("register_student.html")


if __name__ == "__main__":
    app.run()
