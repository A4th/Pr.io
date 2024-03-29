# Generated by Django 4.1.7 on 2023-05-22 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0012_alter_subject_subend_alter_subject_substart'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='User Email')),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='enrolees',
            field=models.ManyToManyField(blank=True, to='hello.webuser'),
        ),
    ]
