# Generated by Django 3.0.6 on 2020-06-07 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qualiCar_API', '0014_auto_20200605_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='part',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='qualiCar_API.Part'),
        ),
    ]
