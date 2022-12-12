from flask import Blueprint, request, jsonify, make_response
import json
from src import db



chef = Blueprint('chef', __name__)

# @chef.route("/chef/chefRecipe")
# def get_recipe():
#     return 
#     <h1> HTML Forms</h1>
#     <form action="/form" method="POST">
#     <label for="recipeID">Recipe ID:</label><br>
#     <input type="int" id="recipeID" name="recipeID" value="0"><br>
#     <label for="recipeName">Recipe Name:</label><br>
#     <input type="text" id="recipeName" name="recipeName" value="blank recipe"><br>
#     <label for="diffLvl">DifficultyLevel:</label><br>
#     <input type="float" id="diffLvl" name="diffLvl" value="0.0"><br>
#     <label for="price">Price:</label><br>
#     <input type="int" id="price" name="price" value="0"><br>
#     <label for="timeToCook">Time to Cook:</label><br>
#     <input type="int" id="timeToCook" name="timeToCook" value="0"><br>
#     <label for="serving">Servings :</label><br>
#     <input type="float" id="serving" name="serving" value="1"><br>
#     <label for="nutritionalValue">Servings :</label><br>
#     <input type="text" id="nutritionalValue" name="nutritionalValue" value="blank value"><br><br>
#     <input type="submit" value="Submit">
#     </form> 

# Chef posts a recipe
@chef.route('/chef/addRecipe', methods=['POST'])
def addRecipe():
   cursor = db.get_db.cursor()
   recipe_id = request.form['recipeID']
   recipe_name = request.form['recipeName']
   diffLvl = request.form['diffLvl']
   price = request.form['price']
   time_cook = request.form['timeToCook']
   recipe_rating = request.form['recipeRating']
   serving = request.form['serving']
   nutritionalValue = request.form['nutritionalValue']
   cursor.execute(f'INSERT INTO recipe(recipe_id, recipe_name, diffLvl, price, time_cook, recipe_rating, serving, nutritionalValue) VALUES(\"{recipe_id}, {recipe_name}, {diffLvl}, {price}, {time_cook}, {recipe_rating}, {serving}, {nutritionalValue}\")')
   db.get_db.commit()
   return "New recipe added!"


# Creates a chef profile
@chef.route('/chef/profile', methods=['POST'])
def createChef():
   cursor = db.get_db.cursor()
   years_of_xp = request.form['yoe']
   specialty_name = request.form['specialtyName']
   prof_rating = request.form['profileRating']
   num_recipes = request.form['numRecipies']
   cursor.execute(f'INSERT INTO recipe (recipe_id, recipe_name, diffLvl, price, time_cook, serving, nutritionalValue) VALUES ({recipe_id}, {recipe_name}, {diffLvl}, {price}, {time_cook}, {serving}, {nutritionalValue}')
   db.get_db.commit()
   return "New profile created!"


# Update a recipe
@chef.route('/chef/editRecipe<recipeID>', methods=['PUT'])
def editRecipe(recipeID):
   cursor = db.get_db.cursor()
   recipe_id = request.form['recipeID']
   recipe_name = request.form['recipeName']
   diffLvl = request.form['diffLvl']
   price = request.form['price']
   time_cook = request.form['timeToCook']
   recipe_rating = request.form['recipeRating']
   serving = request.form['serving']
   nutritionalValue = request.form['nutritionalValue']
   cursor.execute(f'UPDATE recipe(recipe_id, recipe_name, diffLvl, price, time_cook, serving, nutritionalValue) WHERE recipe_id = recipeID SET VALUES({recipe_id}, {recipe_name}, {diffLvl}, {price}, {time_cook}, {serving}, {nutritionalValue}')
   db.get_db.commit()
   return "Recipe Updated!"



# Delete a recipe
@chef.route('/chef/deleteRecipe<recipeID>', methods=['DELETE'])
def deleteRecipe(recipeID):
   cursor = db.get_db.cursor()
   cursor.execute(f'DELETE recipe(recipe_id, recipe_name, diffLvl, price, time_cook, serving, nutritionalValue) WHERE recipe_id = recipeID')
   db.get_db.commit()
   return "Recipe Deleted!"
