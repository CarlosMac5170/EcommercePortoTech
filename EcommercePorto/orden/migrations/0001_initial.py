# Generated by Django 4.0 on 2023-01-27 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0003_alter_product_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electonico')),
                ('address', models.CharField(max_length=250, verbose_name='Dirección')),
                ('postal_code', models.CharField(max_length=20, verbose_name='Código Postal')),
                ('city', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Cantidad')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orden.order', verbose_name='Código de Orden')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='producto.product', verbose_name='Productos')),
            ],
        ),
    ]