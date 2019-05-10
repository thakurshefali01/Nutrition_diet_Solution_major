from django import forms
from nutritionist.models import recipes,recipe_procedure_tb

class recipesForm(forms.ModelForm):
    class Meta():
        model=recipes

        exclude=[
            "category_id",
            "user_email",
            "recipe_id",
            "recipe_name",
            "recipe_image",
            "recipe_description",
            "recipe_procedure",
            "recipe_isactive",
            "recipe_price"

        ]

class recipe_procedure_tbForm(forms.ModelForm):
    class Meta():
        model = recipe_procedure_tb
        exclude = [
            "recipe_id ",
            "user_email ",
            "procedure_id",
            "recipe_name",
            "procedure_discription",
            "prep_time",
            "cook_time",
            "total_time",
            "procedure_ingredients",
            "procedure_instructions",
            "procedure_notes"
                ]
