from unicodedata import category
from rest_framework import generics
from .models import Category, Product
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer, ProductPostSerializer


class ProductListView(generics.ListAPIView):
    """
    API endpoint that allows list of products to be viewed 
    """
    queryset = Product.objects.all()
    filterset_fields = ['category', 'available']
    
    def post(self, request):
        """POST /products"""
        print(request.data)
        if request.data['category']:
            cat = Category.objects.get(name=request.data['category'])
            serializer = ProductSerializer(Product.objects.filter(category=cat.id), many=True)
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


class CategoryDetailView(generics.RetrieveAPIView):
    """
    API endpoint that allows category to be viewed
    """
    queryset =  Category.objects.all()
    serializer_class = CategorySerializer
