# Generated by Django 3.2.5 on 2021-07-26 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invistame', '0002_alter_investimento_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='investimento',
            name='hora',
            field=models.TimeField(default='17:31'),
        ),
    ]
