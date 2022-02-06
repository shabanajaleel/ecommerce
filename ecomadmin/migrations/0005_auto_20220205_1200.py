# Generated by Django 3.2.10 on 2022-02-05 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomadmin', '0004_auto_20220205_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomadmin.role'),
        ),
    ]