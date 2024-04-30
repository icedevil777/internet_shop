from django.shortcuts import render
from rest_framework import permissions, viewsets, generics
from rest_framework import renderers
from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    # permission_classes = [permissions.AllowAny]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    # permission_classes = [permissions.AllowAny]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = CategorySerializer


