# Generated by Django 2.0.6 on 2019-04-03 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_panel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysite_user',
            name='user_lastlogin',
            field=models.CharField(default='', max_length=255),
        ),
    ]
