# Generated by Django 2.0.6 on 2019-04-12 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_panel', '0006_remove_login_details_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysite_user',
            name='otp',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='mysite_user',
            name='otp_time',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]