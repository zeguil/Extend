# Generated by Django 3.2.5 on 2021-11-03 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invistame', '0005_auto_20211101_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investimento',
            name='hora',
            field=models.TimeField(default='22:03'),
        ),
    ]
