$(document).ready(function () {


    // Code for Adding and Removing Ingredients and Steps on Add Recipe Page
    var ingredientField = '<div class="new-ingredient"><div class="input-field col s11"><input placeholder="Next ingredient" type="text" name="ingredients" class="validate" required></div><div class="col s1 icon_left"><a class="btn-floating waves-effect waves-light" id="remove_ingredient"> <i class="material-icons">remove</i></a></div></div>';
    var stepField = '<div class="new-description-step"><div class="input-field col s11"><input placeholder="Next step" type="text" name="recipe_description" class="validate" required></div><div class="col s1 icon_left"><a class="btn-floating waves-effect waves-light" id="remove_description_step"> <i class="material-icons">remove</i></a></div></div>';
    var ingredientField1 = '<div class="new-ingredient"><div class="input-field col s11"><input placeholder="Next ingredient" type="text" name="ingredients" class="validate" required></div><div class="col s1 icon_left"><a class="btn-floating waves-effect waves-light" id="remove_ingredient1"> <i class="material-icons">remove</i></a></div></div>';
    var stepField1 = '<div class="new-description-step"><div class="input-field col s11"><input placeholder="Next step" type="text" name="recipe_description" class="validate" required></div><div class="col s1 icon_left"><a class="btn-floating waves-effect waves-light" id="remove_description_step1"> <i class="material-icons">remove</i></a></div></div>';

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

    // Remove the step from Recipe
    $("body").on("click", "#remove_description_step", function () {
        $(this).parents(".new-description-step").remove();
    });
      // Add Ingredient to Edit Recipe Page
    $("#add_ingredients1").click(function () {
        $("#ingredients3").append(ingredientField1);
        Materialize.updateTextFields();
    });
    // Remove the Ingredient from Edit Recipe Page
    $("body").on("click", "#remove_ingredient1", function () {
        $(this).parents(".new-ingredient").remove();
    });

    // Add Step to Edit Recipe description
    $("#add_description_step1").click(function () {
        $("#recipe_description3").append(stepField1);
        Materialize.updateTextFields();
    });

    // Remove Step from Edit Recipe description
    $("body").on("click", "#remove_description_step1", function () {
        $(this).parents(".new-description-step").remove();
    });
    // Modal  dialog
    $('.modal').modal();



})

  