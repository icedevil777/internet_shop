from rest_framework import generics

from .filters import MyFilter
from .models import Category, Product
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer, ProductPostSerializer
from rest_framework.filters import  OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

  
class ProductListView(generics.ListAPIView):
    """
    API endpoint that allows list of products to be viewed 
    """
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['category', 'available']
    ordering_fields = ['id', 'price']
    filterset_class = MyFilter
    
    def post(self, request):
        """POST /products"""
        if request.data['category']:
            cat = Category.objects.get(name=request.data['category'])
            serializer = ProductSerializer(Product.objects.filter(category=cat.id),
                                           many=True, context={'request': request})
            return Response(serializer.data, status=200)
        return Response(status=400)
        
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
    queryset =  Category.objects.all()
    serializer_class = CategorySerializer
