# Generated by Django 5.0.4 on 2024-05-03 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0007_alter_cart_options_remove_cart_count_alter_cart_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="products",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="user",
        ),
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["name"],
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ["name"]},
        ),
        migrations.RenameIndex(
            model_name="product",
            new_name="shop_produc_id_f21274_idx",
            old_fields=("id", "slug"),
        ),
        migrations.RemoveField(
            model_name="product",
            name="stock",
        ),
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, default="description"),
        ),
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, upload_to="products/%Y/%m/%d"),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="shop.category",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=200),
        ),
        migrations.AddIndex(
            model_name="category",
            index=models.Index(fields=["name"], name="shop_catego_name_289c7e_idx"),
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(fields=["name"], name="shop_produc_name_a2070e_idx"),
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(
                fields=["-created"], name="shop_produc_created_ef211c_idx"
            ),
        ),
        migrations.DeleteModel(
            name="Cart",
        ),
    ]
