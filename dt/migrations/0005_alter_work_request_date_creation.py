# Generated by Django 4.1.1 on 2022-09-24 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dt', '0004_alter_work_request_number_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_request',
            name='date_creation',
            field=models.DateField(),
        ),
    ]