from urllib import response
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import permissions, viewsets, generics
from rest_framework import renderers
from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status


# ___________________ api/v2 _________________________


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs) -> Response:
        print("gjcn")
        return Response


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# ___________________ /api/v1 _________________________


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """

    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer
    # permission_classes = [permissions.AllowAny]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """

    queryset = Category.objects.all().order_by("id")
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
