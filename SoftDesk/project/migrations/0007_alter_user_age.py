# Generated by Django 4.2.3 on 2023-07-30 17:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0006_alter_project_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="age",
            field=models.PositiveIntegerField(
                validators=[django.core.validators.MinValueValidator(1900)]
            ),
        ),
    ]
