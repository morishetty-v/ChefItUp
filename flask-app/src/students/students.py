from flask import Blueprint, request, jsonify, make_response
import json
from src import db


students = Blueprint('recipes', __name__)

# Get all recipes from the DB
@students.route('/recipes', methods=['GET'])
def get_student():
    cursor = db.get_db().cursor()
    cursor.execute('select RecipeName, DifficultyLevel, Price, TimeToCook, Rating, Servings, NutritionalValue from customers')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get recipes ordered by DifficultyLevel
@students.route('/recipes/DifficultyLevel', methods=['GET'])
def get_student():
    cursor = db.get_db().cursor()
    cursor.execute('select * from Recipe order by DifficultyLevel')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get recipes within a budget
@students.route('/recipes/budget/<studentID>', methods=['GET'])
def get_student(studentID,):
    student_cursor = db.get_db().cursor()
    student_cursor.execute('select StudentID from Student where StudentID <= {studentID}')
    #student_row_headers = [x[0] for x in student_cursor.description]
    theStudentData = student_cursor.fetchall()
    budget = theStudentData[0]

    cursor = db.get_db().cursor()
    cursor.execute('select * from Recipe where Price <= {budget}')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get recipes under a certain time to cook
@students.route('/recipes/<max_time>', methods=['GET'])
def get_students(max_time):
    cursor = db.get_db().cursor()
    cursor.execute('select * from Recipe where TimeToCook <= {max_time}')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response