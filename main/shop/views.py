from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import get_serializer
from rest_framework import generics
from .cart import Cart
from .filters import MyFilter
from .models import Category, Product
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer, ProductPostSerializer, СartAddSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class СartAddView(APIView):
    """API endpoint for adding and listing products in cart """
    serializer_class = СartAddSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = Cart(request)
        print(cart.cart)
        return Response(cart.cart, status=status.HTTP_200_OK)

    def post(self, request):
        cart = Cart(request)
        product: Product = get_object_or_404(Product, id=request.data['id'])
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            cart.add(
                product=product,
                quantity=serializer.data['quantity'],
                override_quantity=serializer.data['override']
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ProductListView(generics.ListAPIView):
    """
    API endpoint that allows list of products to be viewed
    """
    serializer_class = ProductPostSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['category', 'available']
    ordering_fields = ['id', 'price']
    filterset_class = MyFilter

    def post(self, request):
        """POST /products"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            category = Category.objects.get(name=serializer.data["category"])
            products = Product.objects.filter(category=category.id)
            serializer = ProductSerializer(products, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductPostSerializer
        return ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    """
    API endpoint that allows product to be viewed
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListView(generics.ListAPIView):
    """
    API endpoint that allows list of categories with products to be viewed
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
    """
    API endpoint that allows category to be viewed
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
