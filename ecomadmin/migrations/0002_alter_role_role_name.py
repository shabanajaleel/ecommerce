# Generated by Django 3.2.10 on 2022-02-05 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
