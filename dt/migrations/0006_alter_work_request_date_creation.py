# Generated by Django 4.1.1 on 2022-09-24 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dt', '0005_alter_work_request_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_request',
            name='date_creation',
            field=models.DateTimeField(),
        ),
    ]
