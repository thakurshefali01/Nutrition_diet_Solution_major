from django import forms
from front_panel.models import MySite_User,User_role

class User_roleForm(forms.ModelForm):
    class Meta():
        model=User_role
        exclude=[
            "role_id",
            "role_name"
        ]

class MySite_UserForm(forms.ModelForm):
    class Meta():
        model=MySite_User

        exclude=[
            "user_name",
            "user_email",
            "user_password",
            "user_mobile",
            "user_gender",
            "user_isactive",
            "user_dob",
            "user_image",
            "user_isavailable",
            "user_isqueue",
            "role_id"
        ]


