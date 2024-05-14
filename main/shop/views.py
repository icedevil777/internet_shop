import copy
from django.http import Http404
from rest_framework import generics
from .cart import Cart
from .filters import MyFilter
from .models import Category, Order, Product, OrderItem
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    ProductPostSerializer,
    СartSerializer,
    СartDetailSerializer,
    OrderSerializer,
    CreateProductSerializer
)


class OrderDetailView(generics.RetrieveAPIView):
    """
    API endpoint that allows one order to be viewed
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreateView(APIView):
    """
    API endpoint for create orders 
    """
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request) -> Response:
        cart = Cart(request)
        items = copy.deepcopy(cart.cart)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            bulk_list = list()
            for item in cart:
                bulk_list.append(
                    OrderItem(
                        order=order,
                        product=item['product'],
                        price=item['price'],
                        quantity=item['quantity']
                    )
                )
            OrderItem.objects.bulk_create(bulk_list)
            cart.clear()
            return Response({"products_in_order": items, "order": serializer.validated_data}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class СartDetailView(APIView):
    """
    API endpoint for delete and update products in cart
    """
    serializer_class = СartDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, pk) -> Product:
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk) -> Response:
        """ Get one product from cart"""
        cart = Cart(request)
        product: Product = self.get_object(pk)
        try:
            product = cart.cart[str(pk)]
            return Response(product, status=status.HTTP_200_OK)
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk) -> Response:
        """ Delete one product from cart"""
        cart = Cart(request)
        product: Product = self.get_object(pk)
        if cart.remove(product):
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk) -> Response:
        """Update on detail page"""
        cart = Cart(request)
        product: Product = self.get_object(pk)
        if not product:
            raise Http404
        else:
            serializer = СartDetailSerializer(data=request.data)
            if serializer.is_valid():
                cart.add(
                    product=product,
                    quantity=serializer.data['quantity'],
                    override_quantity=True
                )
                return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)


class СartView(APIView):
    """
    API endpoint for add and list products in cart and clear all cart
    """
    serializer_class = СartSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request) -> Response:
        """ Get all products from cart"""
        cart = Cart(request)
        price = cart.get_total_price()
        return Response({"price": price, "products": cart.cart}, status=status.HTTP_200_OK)

    def post(self, request) -> Response:
        """Add and Update on list page"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            cart = Cart(request)
            product: Product = get_object_or_404(
                Product, id=request.data['id'])
            cart.add(
                product=product,
                quantity=serializer.data['quantity'],
                override_quantity=serializer.data['override']
            )
            price = cart.get_total_price()
            return Response({"price": price, "products": cart.cart}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request) -> Response:
        """ Delete all products from cart"""
        cart = Cart(request)
        cart.clear()
        return Response(status=status.HTTP_200_OK)


class ProductListView(generics.ListAPIView):
    """
    API endpoint that allows list of products to be viewed
    """
    serializer_class = ProductPostSerializer
    queryset = Product.objects.all()
    filter_backends: list = [DjangoFilterBackend, OrderingFilter]
    filterset_fields: list[str] = ['category', 'available']
    ordering_fields: list[str] = ['id', 'price']
    filterset_class = MyFilter

    def post(self, request) -> Response:
        """POST /products"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            category: Category = Category.objects.get(
                name=serializer.data["category"])
            products = Product.objects.filter(category=category.id)
            serializer = ProductSerializer(
                products, many=True, context={'request': request})
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


class CategoryListCreateView(generics.ListCreateAPIView):
    """
    API endpoint that allows list of categories with products to be viewed
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
    """API endpoint that allows category to be viewed"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductCreateView(generics.CreateAPIView):
    """API endpoint for create products """
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
