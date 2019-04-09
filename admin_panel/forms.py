from django import forms
from admin_panel.models import signup_Admin

class signup_AdminForm(forms.ModelForm):
    class Meta():
        model=signup_Admin
        exclude=[
            "admin_name",
            "admin_email",
            "admin_password",
            "admin_mobile",
            "admin_image",
            "admin_login_time",
            "admin_logout_time"

        ]


