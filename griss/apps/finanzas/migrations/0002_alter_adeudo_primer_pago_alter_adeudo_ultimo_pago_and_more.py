# Generated by Django 5.0.4 on 2024-04-26 20:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adeudo',
            name='primer_pago',
            field=models.DateField(default=datetime.date(2024, 4, 26)),
        ),
        migrations.AlterField(
            model_name='adeudo',
            name='ultimo_pago',
            field=models.DateField(default=datetime.date(2024, 4, 26)),
        ),
        migrations.AlterField(
            model_name='documentosporcobrar',
            name='fecha_de_cobro',
            field=models.DateField(default=datetime.date(2024, 4, 26)),
        ),
        migrations.AlterField(
            model_name='pasivoapagar',
            name='fecha_de_primer_pago',
            field=models.DateField(default=datetime.date(2024, 4, 26)),
        ),
        migrations.AlterField(
            model_name='pasivoapagar',
            name='ultima_fecha',
            field=models.DateField(default=datetime.date(2024, 4, 26)),
        ),
    ]
