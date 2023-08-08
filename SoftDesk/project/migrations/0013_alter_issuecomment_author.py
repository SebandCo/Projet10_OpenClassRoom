# Generated by Django 4.2.3 on 2023-08-08 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0012_alter_issuecomment_issue"),
    ]

    operations = [
        migrations.AlterField(
            model_name="issuecomment",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
