# Generated by Django 2.0.6 on 2019-04-09 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutritionist', '0005_recipes_recipe_isprocedure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe_procedure_tb',
            name='procedure_discription',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='recipe_procedure_tb',
            name='procedure_ingredients',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='recipe_procedure_tb',
            name='procedure_instructions',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='recipe_procedure_tb',
            name='procedure_notes',
            field=models.TextField(default=''),
        ),
    ]