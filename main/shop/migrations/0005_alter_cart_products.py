# Generated by Django 5.0.4 on 2024-04-30 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_cart_product_cart_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(related_name='cart', to='shop.product', verbose_name='Продукты'),
        ),
    ]