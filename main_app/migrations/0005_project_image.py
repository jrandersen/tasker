# Generated by Django 3.1.2 on 2020-11-02 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.CharField(default='add an avatar image', max_length=250),
        ),
    ]
