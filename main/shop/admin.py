from django.contrib import admin
from .models import Category, Product, Cart


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "stock", "available", "created", "updated"]
    list_filter = ["available", "created", "updated"]
    list_editable = ["price", "stock", "available"]
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user", "products_count"]

