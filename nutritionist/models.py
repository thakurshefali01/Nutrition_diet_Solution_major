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