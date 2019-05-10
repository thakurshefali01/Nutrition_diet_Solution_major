from django import forms
from front_panel.models import MySite_User,User_role,Login_details, TemporaryCartTable,SaleTable,ContactTable

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
            "user_sign_up",
            "role_id",
            "otp",
            "otp_time",
            "is_verified"
        ]

class Login_detailsForm(forms.ModelForm):
    class Meta():
        model= Login_details
        exclude=[
            "login_id",
            "login_time",
            "logout_time",
            "user_name"
        ]

class TemporaryTableForm(forms.ModelForm):
    class Meta:
        model = TemporaryCartTable
        exclude=[
            "table_id",
            "email",
            "recipe_id",
            "recipe_name",
            "recipe_image",
            "recipe_description",
            "recipe_price"
        ]

class SaleTableForm(forms.ModelForm):
    class Meta:
        model = SaleTable
        exclude=[
            "table_id",
            "email",
            "recipe_id",
            "recipe_name",
            "recipe_image",
            "recipe_description",
            "recipe_price"
        ]


class ContactTableForm(forms.ModelForm):
    class Meta:
        model =ContactTable
        exclude=[
            "contact_id",
            "contact_name",
            "contact_email",
            "contact_subject",
            "contact_message",
            "contact_time"
        ]