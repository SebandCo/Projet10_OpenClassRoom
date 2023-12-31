# Generated by Django 4.2.3 on 2023-07-29 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0005_issue_author_issue_created_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="type",
            field=models.CharField(
                choices=[
                    ("Back-end", "Back-end"),
                    ("Front-end", "Front-end"),
                    ("iOS", "iOS"),
                    ("Android", "Android"),
                ],
                max_length=30,
            ),
        ),
    ]
