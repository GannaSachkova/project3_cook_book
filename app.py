import os
from flask import Flask, render_template, redirect, request, url_for, request, session, g, abort, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId






app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cook_book'

app.config["MONGO_URI"] = os.getenv(
    'MONGO_URI', 'mongodb+srv://dorogaya:Ganna1810@cluster0-1ulil.mongodb.net/cook_book?retryWrites=true&w=majority')

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

# Recipes

@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html",  recipes=mongo.db.recipes.find(), categories=mongo.db.categories.find(), cuisine=mongo.db.cuisine_type.find())


@app.route('/addrecipe')
def addrecipe():
    return render_template('add_recipe.html', categories=mongo.db.categories.find(), cuisine=mongo.db.cuisine_type.find())


@app.route('/insertrecipe', methods=['POST'])
def insertrecipe():
    recipes = mongo.db.recipes
    the_whole_recipe = {
                'recipe_title': request.form.get('recipe_title'),
                'category_name': request.form.get('category_name'),
                'cuisine_type': request.form.get('cuisine_type'),
                'ingredients':  request.form.getlist('ingredients'),
                'recipe_description': request.form.getlist('recipe_description'),
                'prep_time': request.form.get('prep_time'),
                'cook_time': request.form.get('cook_time'),
                'total_time': request.form.get('total_time'),
                'serving':  request.form.get('serving')
        }
    post_id = recipes.insert_one(the_whole_recipe).inserted_id
    the_recipe = recipes.find_one({"_id": ObjectId(post_id)})
    return render_template('recipe_main.html', recipe=the_recipe)


@app.route('/editrecipe/<recipe_id>')
def editrecipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    all_cuisines = mongo.db.cuisine_type.find()
    return render_template('edit_recipe.html', recipe=the_recipe, categories=all_categories, cuisine=all_cuisines)


@app.route('/updaterecipe/<recipe_id>', methods=["POST"])
def updaterecipe(recipe_id):
    recipes = mongo.db.recipes
    
    recipes.update({'_id': ObjectId(recipe_id)},
                       {"$set": {
                           'recipe_title': request.form.get('recipe_title'),
                           'cuisine_type': request.form.get('cuisine_type'),
                           'category_name': request.form.get('category_name'),
                           'ingredients': request.form.getlist('ingredients'),
                           'recipe_description': request.form.getlist('recipe_description'),
                           'prep_time': request.form.get('prep_time'),
                           'cook_time': request.form.get('cook_time'),
                           'total_time': request.form.get('total_time'),
                           'serving': request.form.get('serving')
                       }})
    the_recipe =recipes.find_one({"_id": ObjectId(recipe_id)})
          
    return render_template('recipe_main.html', recipe=the_recipe)



@app.route('/recipemainpage/<recipe_id>', methods=['GET'])
def recipemainpage(recipe_id):
    recipeCategory=mongo.db.categories.find(),
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_cuisines = mongo.db.cuisine_type.find()
    return render_template('recipe_main.html', categories=recipeCategory,
         recipe=the_recipe, cuisine=all_cuisines)
       

@app.route('/deleterecipe/<recipe_id>')
def deleterecipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))




#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
# CUISINE

@app.route('/get_cuisines')
def get_cuisines():
    return render_template('cuisines.html', cuisine=mongo.db.cuisine_type.find())


@app.route('/addcuisine')
def addcuisine():
    return render_template('add_cuisine.html', cuisine=mongo.db.cuisine_type.find())


@app.route('/insertcuisine', methods=['POST'])
def insertcuisine():
    cuisines = mongo.db.cuisine_type
    cuisines.insert_one(request.form.to_dict())
    return redirect(url_for('get_cuisines'))


@app.route('/editcuisine/<cuisine_id>')
def editcuisine(cuisine_id):
    return render_template('edit_cuisine.html', cuisine=mongo.db.cuisine_type.find_one({'_id':ObjectId(cuisine_id)}))



@app.route('/updatecuisine/<cuisine_id>', methods=['POST'])
def updatecuisine(cuisine_id):
    cuisine=mongo.db.cuisine_type
    cuisine.update({'_id': ObjectId(cuisine_id) },
                        {"$set": {
                        'cuisine_type': request.form.get('cuisine_type')
                        }})   

    return redirect(url_for('get_cuisines'))



@app.route('/inserteditcuisine', methods=['POST'])
def inserteditcuisine():
    cuisines=mongo.db.cuisine_type
    cuisines.insert_one(request.form.to_dict())
    return redirect(url_for('get_cuisines'))




@app.route('/deletecuisine/<cuisine_id>')
def deletecuisine(cuisine_id):
    mongo.db.cuisine_type.remove({'_id': ObjectId(cuisine_id)})
    return redirect(url_for('get_cuisines'))



@app.route('/insertcuisineedit', methods=['POST'])
def insertcuisineedit():
    cuisines = mongo.db.cuisine_type
    cuisines.insert_one(request.form.to_dict())
    return redirect(url_for('get_cuisines'))

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
# Search Recipe


@app.route('/findrecipe')
def findrecipe():
    categories = mongo.db.categories.find()
    cuisines = mongo.db.cuisine_type.find()
    return render_template("find_recipe.html", cuisine=cuisines, categories=categories)


@app.route('/filterrecipes', methods=['POST', 'GET'])
def filterrecipes():
    recipes = mongo.db.recipes
    cuisine_type = request.form.get('cuisine_type')
    category_name = request.form.get('category_name')

    results_category_name = recipes.find({"category_name": category_name})
    results_cuisine_type = recipes.find({"cuisine_type": cuisine_type})
    # result_cook_time=recipes.find({ "cook_time":cook_time})
    # number=recipes.count({ "cuisine_type":cuisine_type })
    # number1=recipes.count({ "category_name":category_name })
    return render_template("results.html", results_category_name=results_category_name, results_cuisine_type=results_cuisine_type)

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
