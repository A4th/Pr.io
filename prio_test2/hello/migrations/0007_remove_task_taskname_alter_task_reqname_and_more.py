# Generated by Django 4.1.7 on 2023-05-10 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_alter_task_taskname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='taskName',
        ),
        migrations.AlterField(
            model_name='task',
            name='reqName',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Requirement',
        ),
    ]