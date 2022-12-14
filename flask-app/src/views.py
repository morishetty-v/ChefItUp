from flask import Blueprint, request, jsonify, make_response
import json
from src import db

views = Blueprint('views', __name__)

# This is a sample route for the /test URI.  
# as above, it just returns a simple string. 
@views.route('/test')
def tester():
    return "<h1>this is a test!</h1>"