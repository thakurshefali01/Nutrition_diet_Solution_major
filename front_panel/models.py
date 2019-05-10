from django.db import models


# Create your models here.
class User_role (models.Model):
    role_id=models.AutoField(primary_key=True)
    role_name=models.CharField(max_length=225,default="",unique=True)

class MySite_User(models.Model):
    role_id=models.ForeignKey(User_role,on_delete=models.CASCADE,default="")
    user_name=models.CharField(max_length=255)
    user_email=models.EmailField(primary_key=True,max_length=225,default="")
    user_password=models.CharField(max_length=20,default="")
    user_mobile=models.BigIntegerField()
    user_gender=models.CharField(max_length=10,default="")
    user_isactive=models.BooleanField(default=True)
    user_dob=models.CharField(max_length=255,default="")
    user_image=models.CharField(max_length=255,null=True)
    user_isavailable=models.BooleanField(default=True)
    user_isqueue=models.BooleanField(default=False)
    user_sign_up=models.CharField(max_length=255,default="")
    otp=models.CharField(max_length=255,default="",null=True)
    otp_time=models.CharField(max_length=255,default="",null=True)
    user_token=models.CharField(max_length=255,default="")
    is_verified = models.BooleanField(default=False)

class Login_details(models.Model):
    login_id = models.AutoField(primary_key=True)
    login_time = models.CharField(max_length=255)
    logout_time = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)


class TemporaryCartTable(models.Model):
    table_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, default="", null=True)
    recipe_id = models.CharField(max_length=255, default="", null=True)
    recipe_name = models.CharField(max_length=225, default="", null=True)
    recipe_image = models.CharField(max_length=225, default="", null=True)
    recipe_description = models.CharField(max_length=225, default="", null=True)
    recipe_price = models.CharField(max_length=225, null=True)


class SaleTable(models.Model):
    table_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, default="", null=True)
    recipe_id = models.CharField(max_length=255, default="", null=True)
    recipe_name = models.CharField(max_length=225, default="", null=True)
    recipe_image = models.CharField(max_length=225, default="", null=True)
    recipe_description = models.CharField(max_length=225, default="", null=True)
    recipe_price = models.CharField(max_length=225, null=True)

class ContactTable(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=225, default="")
    contact_email = models.CharField(max_length=225, default="")
    contact_subject = models.CharField(max_length=225, default="",null=True)
    contact_message = models.TextField(default="")
    contact_time = models.CharField(max_length=225 ,default="")