from django import forms
from nutritionist.models import AddExercise,Procedure_exercise


class Add_exerciseForm(forms.ModelForm):
    class Meta():
        model=AddExercise

        exclude=[
            "exercise_id",
            "user_email",
            "add_exercise_id",
            "exercise_name",
            "exercise_image",
            "exercise_discription",
            "exercise_price",
            "exercise_isprocedure"
            ]
class Procedure_exerciseForm(forms.ModelForm):
    class Meta():
        model=Procedure_exercise

        exclude = [
            "add_exercise_id",
            "user_email",
            "ex_procedure_id",
            "exercise_name",
            "parts_included",
            "equipment_required",
            "steps_included"
        ]
