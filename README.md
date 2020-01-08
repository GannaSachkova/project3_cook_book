Code Institute Cook Book
======================================


**This project is designed as a platform on which to demonstrate my data centric development skills.**


Demo
-----------------------------------------


A live demo of the website you can be found [here](https://cook-book-project3.herokuapp.com/)


UX
-----------------------------------------

Cook Book is a recipe-organizer that exists in a NoSQL Mongo database and allows you organize your recipes: add/edit recipes, search or even delete them.

My goal in the design was to make it as easy as possible to access information on the site while striving for a minimalist design. So the website does this in a simple intuitive way with easy navigation, minimal fields. This application is user friendly and interactive.
Details of the UX design is available in the wireframes folder. This folder contains web page escise pages of the application.

Features
-----------------------------------------


#### Existing Features


##### Adding a recipe

From the home page, you can proceed to the add recipe form by clicking the clearly defined "Add Recipe" button or using the "Add Recipe" navbar tab (as you can anywhere across the website). The form has 9 fields to complete. Each field is clearly labeled.  Only a few of them are required fields ( recipe title, ingredients and recipe description). The other fields aren’t required to fill. So, the form can't be submitted until these important fields are complete. 
 
The "Cuisine Type" field is a dropdown menu where you can choose from the cuisine types already exist in the database. If this is not already in the database you can add a new cuisine type by clicking on the clearly labeled button next to this field. This link leads to a page where a new cuisine can be added to the database. And once this form is submitted the website will redirect you back to the add recipe page. The submit button is clearly marked at the bottom of the page. By clicking this button the form will update the database and the user will be redirected to the All Recipes page where you can view your recipe.

##### Finding a recipe
From the "Home" page you can proceed to the "Find Recipe" page by clicking the clearly defined "Find Recipe" button or using the "Find Recipe" navbar tab (as you can anywhere across the website). A page is effectively a form where a user can choose from 2 different fields (cuisine type and category) to filter the full list of recipes by. These can be used alone or together however if used together you get all the results from each filter. If the form is submitted without choosing any parameters all recipes will be displayed. Once the parameters are chosen the form is submitted by clicking the clearly labeled "Find Recipe" button beneath the form. This will redirect the user to the "Results Page" displaying all results.
##### Editing/Deleting a recipe
Recipes are displayed on "All Recipes" page. Recipies are displayed as an accordion where the recipe name, category, cuisine type, total time, preparation time and cook time are all displayed without opening. Located to the right of each this information there are 3 clearly labeled buttons, "View", "Edit" and "Delete".  To delete a recipe a user would simply click on the recipe that would like to delete and the recipe will be removed permanently from the database. To edit a recipe the user would click the "Edit" button. This will redirect the user to an identical "Edit Recipe" page with the fields that already are being filled in with the current recipe information. When all needed fields have been edited the user would just click the "Update Recipe" button. Then the user will be redirected to the thankful page and then back to the "Home" page. If the user decides to keep going changes to the recipe you can click the "Cancel" button found next to the "Update recipe" button and the user will stay on the current page.

##### View all recipes page
Recipes are displayed as an accordion list. When initially viewed this list will show each recipe by its name, category, cuisine type, total time, preparation time and cook time. Upon clicking a recipe this opens the accordion to reveal a new accordion list with "ingredients" and "description" as the 2 list items. These new accordions can then be expanded to display their content. 

####  Future Features
*	**Images**– I would like to add them to the each main recipe page. 
*	**Comments** - to allow users to leave a detailed comment about a recipe.
*	**User log Up / Log In** - I would like to add it to the web site later. I suppose it is important part for each website to secure private information. 
*	**Share links** -I would like to add share functionality so people can share thier favourite recipes via social media/email etc.  
*	**Filter** - I would like to add functionality to the filter. For now it is not working correctly. 
*	**Modal forms** -  I would like to add the modal forms to the “Delete” buttons with related fields that ask the user if he/she sure to delete related information from recipe. 
*	**Shopping List** - A feature for users to allows automatically generate shopping list from liked recipes by clicking to checkbox to let a user select one or more options of their choices.  The chosen items will be sorted by categories or generate a separate shopping list for each recipe.  

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

There was no automated testing used for this project. Each function has been tested thoroughly manually. There are 6 main functions across the website.

**1 - Add recipe**
Go to the "Add Recipe" page and try to submit a recipe with one or more of the incompleted fields - the form will not submit and an error message will display on the screen showing the user which fields require revisiting.

**2 - Edit recipe**
Go to the "Edit Recipe" page to edit recipe form or leave it without any changes.  Then click the button “Update Recipe” if you finished. Or click on the “Cancel” button to keep going to do necessaries changes. The original recipe will be updated with included the changes. 

**3 - View Recipe** To view and  familiarize yourself with the recipe: with necessaries ingredients an directions to cook - go to "All Recipes" page and click the "View" button that redirect you to the recipe page.

**4 - Delete recipe**
To find a recipe that you would like to delete: go to "All Recipes" page and click the "Delete" button.  The recipe will be no longer show as it has been removed from the database. 


**5 - Add cuisine type**
Click the "Add a New Cuisine" button on the “Add Recipe” page. You will redirect on a new page “Add a New Cuisine”, where you can add the new cuisine. To confirm it - click on “Add Cuisine” button and the new cuisine type will be added to the database. Also, it appears in all “All Cuisine Type” dropdown menus across the website.

**6 - Edit cuisine type**
To find cuisine type that you would like to delete: go on the "All Recipes". Then click the “Edit” button and you will redirect to the “Edit Recipe” page. There you need to find and click a button “View all Cuisines. The page “Cuisines” will be open. There you need to find cuisine type that you would like to edit or delete. 
If you select the option “Delete” – the selected cuisine will be no longer show on the page because it will be permanently removed from the database and all related dropdown menus across the website.
If you select the button with “Edit” icon – it sends you to a new page “Edit Cuisine”, where you can edit cuisine type and click onto the “Update cuisine” button. It will be updated with included changes.

**7 - Find recipe** 
Go to the "Find Recipe" page and select a filtering parameter then click the button “Find recipe”. It will show a list of results for each chosen parameter. If no matched results – will show a blank page with a "back to search" button.


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
