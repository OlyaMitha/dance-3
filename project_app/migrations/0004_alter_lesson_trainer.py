# Generated by Django 4.0.4 on 2022-05-19 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0003_trainer_alter_lesson_trainer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='trainer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='project_app.trainer'),
        ),
    ]
