# Generated by Django 3.0.6 on 2020-05-29 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qualiCar_API', '0007_auto_20200529_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='part',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='qualiCar_API.Part'),
        ),
    ]
