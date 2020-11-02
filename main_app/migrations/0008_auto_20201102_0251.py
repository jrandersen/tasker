# Generated by Django 3.1.2 on 2020-11-02 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20201102_0246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.URLField(default='https://semantic-ui.com/images/avatar/large/steve.jpg', max_length=250),
        ),
    ]