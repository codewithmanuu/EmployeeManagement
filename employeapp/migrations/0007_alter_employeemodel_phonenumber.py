# Generated by Django 4.2.2 on 2023-06-23 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeapp', '0006_alter_employeemodel_designation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='phonenumber',
            field=models.BigIntegerField(),
        ),
    ]
