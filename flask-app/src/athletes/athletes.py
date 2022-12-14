from flask import Blueprint, request, jsonify, make_response
import json
from src import db


athletes = Blueprint('athletes', __name__)

# Get all recipes from the DB
@athletes.route('/athletes', methods=['GET'])
def get_athletes():
    cursor = db.get_db().cursor()
    cursor.execute('select * from Recipe')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get recipes that fit under a certain caloric goal
@athletes.route('/athletes/CaloricGoal/<AthleteID>', methods=['GET'])
def get_by_calories(athleteID):
    athlete_cursor = db.get_db().cursor()
    athlete_cursor.execute('select Calories from Athlete where AthleteID <= {athleteID}')
    theAthleteData = athlete_cursor.fetchall()
    calories = theAthleteData[0]
    
    cursor = db.get_db().cursor()
    cursor.execute('select * from Recipe where NutrionalValue <= {calories}')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response