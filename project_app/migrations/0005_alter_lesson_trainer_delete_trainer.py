# Generated by Django 4.0.4 on 2022-05-19 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0004_alter_lesson_trainer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='trainer',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Trainer',
        ),
    ]
