# Generated by Django 3.2.5 on 2021-11-03 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invistame', '0006_alter_investimento_hora'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='aniversario',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='contato',
            name='telefone',
            field=models.CharField(default=None, max_length=13),
        ),
        migrations.AlterField(
            model_name='investimento',
            name='hora',
            field=models.TimeField(default='22:23'),
        ),
    ]
