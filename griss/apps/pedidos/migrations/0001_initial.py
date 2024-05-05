# Generated by Django 5.0.4 on 2024-04-25 07:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_entrega', models.DateField(default=datetime.date(2024, 4, 25))),
                ('fecha_de_pedido', models.DateField(default=datetime.date(2024, 4, 25))),
                ('tipo_de_pedido', models.CharField(choices=[('producto_del_inventario', 'productos_del_inventario'), ('productos_por_encargo', 'productos_por_encargo')], default='producto_del_inventario', max_length=23)),
                ('lugar_de_entrega', models.CharField(default='en_tienda', max_length=255)),
                ('nombre_del_cliente', models.CharField(default='####', max_length=255)),
                ('numero_de_telefono', models.CharField(default='##########', max_length=8)),
                ('productos', models.ManyToManyField(related_name='pedidos', to='inventario.producto')),
            ],
        ),
    ]