Code Institute Cook Book
======================================


**This project is designed as a platform on which to demonstrate my data centric development skills.**


Demo
-----------------------------------------


A live demo of the website you can be found [here](https://cook-book-project3.herokuapp.com/)


UX
-----------------------------------------

Cook Book is a recipe-organizer that exists in a NoSQL Mongo database and allows you to organize your recipes: add/edit recipes, search or even delete them.

My goal in the design was to make it as easy as possible to access information on the site while striving for a minimalist design. So the website does this in a simple intuitive way with easy navigation, minimal fields. This application is user-friendly and interactive.
Details of the UX design is available in the wireframes folder. This folder contains web page excise pages of the application.

Features
-----------------------------------------


#### Existing Features


##### Adding a recipe
From the home page, you can proceed to the add recipe form by clicking the clearly defined "Add Recipe" button or using the "Add Recipe" navbar tab (as you can anywhere across the website). The form has 9 fields to complete. Each field is clearly labeled.  Only a few of them are required fields ( recipe title, ingredients and recipe description). The other fields aren’t required to fill. So, the form can't be submitted until these important fields are complete. 
 
The "Category" and "Cuisine Type" fields are a dropdown menu where you can choose from the cuisine/category types already exist in the database. 

The submit button is clearly marked at the bottom of the page. By clicking this button the form will update the database and the user will be redirected to the main recipe page where you can view your it more detailed.

##### Finding a recipe
From the "Home" page you can proceed to the "Find Recipe" page by clicking the clearly defined "Find Recipe" button or using the "Find Recipe" navbar tab (as you can anywhere across the website). A page is effectively a form where a user can choose from 2 different fields (cuisine type and category) to filter the full list of recipes by. These can be used alone or together however if used together you get all the results from each filter. If the form is submitted without choosing any parameters all recipes will be displayed. Once the parameters are chosen the form is submitted by clicking the clearly labeled "Find Recipe" button beneath the form. This will redirect the user to the "Results Page" displaying all results.

##### Editing/Deleting a recipe
To find the recipe you would like to “EDIT” or “DELETE”  - go to the "All Recipes" page and click on the recipe title that you would like to edit/delete. On the top of this page you can see two buttons: "EDIT" and "DELETE". To edit recipe: click on the "Edit" button.  After some changes click on the “Update Recipe” button. Or if you change your mind - click on the “Cancel” button. It redirects you back to the main recipe page.  

##### View all recipes page
Recipes are displayed as the card list. When initially viewed on this card list you will show each recipe by its name, category, cuisine type and cook time. Upon clicking a recipe title this opens the main page of the recipe with a detailed description of it.

####  Future Features
*	**Images**– I would like to add them to each main recipe page. 
*	**Comments** - to allow users to leave a detailed comment about a recipe.
*	**User log Up / Log In** - I would like to add it to the web site later. I suppose it is an important part of each website to secure private information. 
*	**Share links** -I would like to add share functionality so people can share their favorite recipes via social media/email etc.    
*	**Shopping List** - A feature for users to allows automatically generate shopping lists from liked recipes by clicking to the checkbox to let a user select one or more options of their choices.  The chosen items will be sorted by categories or generate a separate shopping list for each recipe.  

Technologies Used
-----------------------------------------
The website is designed using following technologies:
*	HTML
*	CSS
*	JavaScript
*	Python
*	Flask
*	Mongodb
*	Jquery
*	Font Awesome library
*	Materializecss 0.100.2
*	Google Fonts
*	Github
*	Gitpod
*	Heroku

Testing
-----------------------------------------

## Testing
Resources & Tools Used for Testing

* HTML [W3 HTML Validator](https://validator.w3.org/)

* CSS  [W3 CSS Validator](https://jigsaw.w3.org/css-validator/)

* online Beautifier [freeformatter.com](https://www.freeformatter.com) and [CSS Formatter](https://www.cleancss.com)

The application was build using Google Chrome.

This project was tested for responsiveness using the Chrome Developer Tools.



There are 5 main functions across the application.

**1 - Add recipe**
Go to the "Add Recipe" page and try to submit a recipe with one or more of the incompleted fields - the form will not submit and an error message will display on the screen showing the user which fields require revisiting.

**2 - Edit recipe**
Go to the "All Recipe" page and click on the recipe title that you would like to see or to be familiar with. On the top of this page you can see two buttons: "EDIT" and "DELETE". To edit recipe: click on the "Edit" button.  After some changes click on the “Update Recipe” button. Or if you change your mind - click on the “Cancel” button. It redirects you to the main recipe page.

**3 - View Recipe** To view and familiarize yourself with the recipe: with necessaries ingredients an directions to cook - go to the "All Recipes" page and click the recipe title that you would like to be familiar with. 

**4 - Delete recipe**
To delete recipe you can from the main recipe page. You just need to click on the "DELETE" button on the top of that page.  When you click on it - a new window opens when you need to submit your action: delete or leave it in the database. After clicking "DELETE" the recipe will be no longer show as it has been removed from the database. 

**5 - Find recipe** 
Go to the "Find Recipe" page and select a filtering parameter then click the button “Find recipe”. It will show a list of results for each chosen parameter. If no matched results – will show a blank page with a "BACK TO SEARCH" button.


Deployment
----------------------------------------
Deployment and source control was carried out via GitHub and Heroku. The repository location is as follows: [https://github.com/GannaSachkova/project3_cook_book](https://github.com/GannaSachkova/project3_cook_book)

Heroku App Location is as follows: [https://cook-book-project3.herokuapp.com/](https://cook-book-project3.herokuapp.com/)


Credits
----------------------------------------

**Content**
+ Almost all project content was written by me following the video instructions of the Code Institute instructors.

+ Background image of main page was taken from internet.

+ Some of the page elements (e.g. navbar, footer..etc) has been taken from [Materialize](http://archives.materializecss.com/0.100.2/).

+ Some of the recipes has been copied from [BBC_Food](https://www.bbc.com/food/recipes)


**Acknowledgements**
All materials and content in this project are solely for educational purposes.

**Contact**

Created by [Ganna Sachkova](mailto:dorogaya1810@gmail.com).
