from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from app import app
import os
import csv
import sys

db = SQLAlchemy(app)
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'app.db')


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_number = db.Column(db.String(30), index=True, unique=True)
    course_title = db.Column(db.String(30), index=True, unique=True)


class RegisteredStudent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True)
    grade = db.Column(db.String(3), index=True, unique=True)


