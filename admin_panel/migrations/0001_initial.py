# Generated by Django 2.0.6 on 2019-04-01 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup_Admin',
            fields=[
                ('admin_name', models.CharField(max_length=255)),
                ('admin_email', models.EmailField(default='', max_length=225, primary_key=True, serialize=False)),
                ('admin_password', models.CharField(default='', max_length=20)),
                ('admin_mobile', models.BigIntegerField()),
                ('admin_image', models.CharField(max_length=255, null=True)),
                ('admin_login_time', models.CharField(default='', max_length=255)),
                ('admin_logout_time', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
