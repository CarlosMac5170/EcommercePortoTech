# Generated by Django 4.0 on 2023-01-16 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'producto', 'verbose_name_plural': 'productos'},
        ),
    ]
