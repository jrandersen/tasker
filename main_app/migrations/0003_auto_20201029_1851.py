# Generated by Django 3.1.2 on 2020-10-29 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201029_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='date',
            field=models.DateField(),
        ),
    ]