# Generated by Django 3.2.5 on 2021-07-26 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invistame', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investimento',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
