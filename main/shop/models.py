from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """ Category of products """
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name']),]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True, default='description')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self) -> str:
        return self.name


# class Order(models.Model):
#     """
#     Model for saving data  about orders
#     """

#     user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name="Покупатель")

#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Покупатель")
#     data_created = models.DateTimeField(
#         auto_now_add=True, verbose_name="Дата оформления заказа"
#     )

#     products = models.ManyToManyField(Product, verbose_name="Продукты")

#     @property
#     def products_count(self) -> int:
#         return self.products.count()

#     class Meta:
#         verbose_name = "Заказ"
#         verbose_name_plural = "Заказы"

#     def __str__(self) -> str:
#         return f"Заказ {self.user}"
