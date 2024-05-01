from django_filters import rest_framework as filters
from .models import Product


class MyFilter(filters.FilterSet):
    
    class Meta:
        model = Product
        fields = {
            'price': ['gte', 'lte'],
            'name': ['iexact']
        }