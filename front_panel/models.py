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
    user_lastlogin=models.CharField(max_length=255,default="")
