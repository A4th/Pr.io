# Generated by Django 4.2.1 on 2023-05-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hello", "0020_delete_webuser"),
    ]

    operations = [
        migrations.AddField(
            model_name="subject",
            name="subjDays",
            field=models.JSONField(null=True),
        ),
    ]