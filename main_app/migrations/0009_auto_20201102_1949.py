# Generated by Django 3.1.2 on 2020-11-02 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20201102_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='createdDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
