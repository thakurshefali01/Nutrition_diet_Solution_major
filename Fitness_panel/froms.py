from django import forms
from nutritionist.models import AddExercise


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
            "exercise_price"
            ]
