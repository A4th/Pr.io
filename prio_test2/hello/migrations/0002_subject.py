# Generated by Django 4.1.7 on 2023-04-25 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subName', models.CharField(max_length=50)),
                ('numUnits', models.IntegerField()),
                ('subStart', models.DateTimeField()),
                ('subEnd', models.DateTimeField()),
            ],
        ),
    ]