from django.db import models
from django.contrib.auth.models import  User

class Category(models.Model):
    """ Category of products """
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    """ Product in the Category"""
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self) -> str:
        return self.name


class Cart(models.Model):
    """
    Model for saving data in cart of user with products
    """

    user = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, verbose_name="Покупатель"
    )
    products = models.ManyToManyField(Product, verbose_name="Продукты")
    
    @property
    def products_count(self) -> int:
        return self.products.count()
    
    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    def __str__(self) -> str:
        return f"Корзина {self.user}"


