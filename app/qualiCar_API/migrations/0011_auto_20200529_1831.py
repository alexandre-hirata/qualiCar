# Generated by Django 3.0.6 on 2020-05-29 18:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qualiCar_API', '0010_auto_20200529_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='create_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 29, 18, 31, 10, 896622, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='incident',
            name='last_change_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 29, 18, 31, 10, 896646, tzinfo=utc)),
        ),
    ]
