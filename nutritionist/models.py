from django.db import models
from front_panel.models import MySite_User
# Create your models here.

class category(models.Model):

    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=225,default="",unique=True)

class recipes(models.Model):
    category_id = models.ForeignKey(category,on_delete=models.CASCADE,default="")
    user_email = models.ForeignKey(MySite_User,on_delete= models.CASCADE,default="")
    recipe_id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=225)
    recipe_image = models.CharField(max_length=225,null=True)
    recipe_description = models.CharField(max_length=225, default="")
    recipe_procedure = models.TextField(default="")
    recipe_isactive = models.BooleanField(default=True)
    recipe_isProcedure = models.BooleanField(default=False)
    recipe_price=models.CharField(max_length=225, null=True)


class recipe_procedure_tb(models.Model):
    recipe_id = models.ForeignKey(recipes,on_delete=models.CASCADE,default="")
    user_email = models.ForeignKey(MySite_User, on_delete=models.CASCADE, default="")
    procedure_id=models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=225)
    procedure_discription = models.TextField(default="")
    prep_time = models.CharField(max_length=225)
    cook_time =models.CharField(max_length=225)
    total_time =models.CharField(max_length=225)
    procedure_ingredients = models.TextField(default="")
    procedure_instructions = models.TextField(default="")
    procedure_notes = models.TextField(default="")


class ExerciseCategory(models.Model):
    exercise_id = models.AutoField(primary_key=True)
    exercise_category = models.CharField(max_length=225, default="", unique=True)


class AddExercise(models.Model):
    exercise_id = models.ForeignKey(ExerciseCategory, on_delete=models.CASCADE, default="")
    user_email = models.ForeignKey(MySite_User, on_delete=models.CASCADE, default="")
    add_exercise_id=models.AutoField(primary_key=True)
    exercise_name=models.CharField(max_length=225, default="")
    exercise_image=models.CharField(max_length=225,default="")
    exercise_discription=models.CharField(max_length=225, default="")
    exercise_price = models.CharField(max_length=225, null=True)
    exercise_isProcedure = models.BooleanField(default=False)


class Procedure_exercise(models.Model):
    add_exercise_id = models.ForeignKey(AddExercise, on_delete=models.CASCADE, default="")
    user_email = models.ForeignKey(MySite_User, on_delete=models.CASCADE, default="")
    ex_procedure_id=models.AutoField(primary_key=True)
    exercise_name=models.CharField(max_length=225, null=True)
    parts_included=models.CharField(max_length=225, null=True)
    equipment_required=models.CharField(max_length=225, null=True)
    steps_included=models.TextField(default="")

