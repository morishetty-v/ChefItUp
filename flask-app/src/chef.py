from flask import Blueprint, request, jsonify, make_response
import json
from src import db



chef = Blueprint('chef', __name__)

@chef.route("/chef/chefRecipe")
def get_recipe():
    return 
    <h1> HTML Forms</h1>
    <form action="/form" method="POST">
    <label for="recipeID">Recipe ID:</label><br>
    <input type="int" id="recipeID" name="recipeID" value="0"><br>
    <label for="recipeName">Recipe Name:</label><br>
    <input type="text" id="recipeName" name="recipeName" value="blank recipe"><br>
    <label for="diffLvl">DifficultyLevel:</label><br>
    <input type="float" id="diffLvl" name="diffLvl" value="0.0"><br>
    <label for="price">Price:</label><br>
    <input type="int" id="price" name="price" value="0"><br>
    <label for="timeToCook">Time to Cook:</label><br>
    <input type="int" id="timeToCook" name="timeToCook" value="0"><br>
    <label for="serving">Servings :</label><br>
    <input type="float" id="serving" name="serving" value="1"><br>
    <label for="nutritionalValue">Servings :</label><br>
    <input type="text" id="nutritionalValue" name="nutritionalValue" value="blank value"><br><br>
    <input type="submit" value="Submit">
    </form> 

# Chef posts a recipe
@chef.route('/chef/chefRecipe', methods=['POST'])
def addRecipe():
   recipe_id = request.form['recipeID']
   recipe_name = request.form['recipeName']
   diffLvl = request.form['diffLvl']
   price = request.form['price']
   time_cook = request.form['timeToCook']
   serving = request.form['serving']
   nutritionalValue = request.form['nutritionalValue']
   cursor = db.get_db.cursor()
   cursor.connection.commit()
   cursors.execute(f'INSERT INTO recipe (recipe_id, recipe_name, diffLvl, price, time_cook, serving, nutritionalValue) VALUES ({recipe_id}, {recipe_name}, {diffLvl}, {price}, {time_cook}, {serving}, {nutritionalValue}')
   return get_all()