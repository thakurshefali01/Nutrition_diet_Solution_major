# Generated by Django 2.0.6 on 2019-05-16 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nutritionist', '0003_auto_20190515_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedure_exercise',
            name='add_exercise_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='nutritionist.AddExercise'),
        ),
    ]