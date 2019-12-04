$(document).ready(function () {


    // Code for Adding and Removing Ingredients and Steps on Add Recipe Page
    var ingredientField = '<div class="new-ingredient"><div class="input-field col s11"><input placeholder="Next ingredient" type="text" name="ingredients" class="validate" required></div><div class="col s1"><a class="btn-floating waves-effect waves-light" id="remove_ingredient"> <i class="material-icons">remove</i></a></div></div>';
    var stepField = '<div class="new-description-step"><div class="input-field col s11"><input placeholder="Next step" type="text" name="recipe_description" class="validate" required></div><div class="col s1"><a class="btn-floating waves-effect waves-light" id="remove_description_step"> <i class="material-icons">remove</i></a></div></div>';

    // Add Ingredient to Recipe
    $("#add_ingredients").click(function () {
        $("#ingredients").append(ingredientField);
        Materialize.updateTextFields();
    });
    // Remove the Ingredient from Recipe
    $("body").on("click", "#remove_ingredient", function () {
        $(this).parents(".new-ingredient").remove();
    });

    // Add Step to Recipe description
    $("#add_description_step").click(function () {
        $("#recipe_description1").append(stepField);
        Materialize.updateTextFields();
    });

    // Remove the Ingredient from Recipe
    $("body").on("click", "#remove_description_step", function () {
        $(this).parents(".new-description-step").remove();
    });



})