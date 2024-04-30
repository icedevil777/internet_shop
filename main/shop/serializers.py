from rest_framework import serializers

from .models import Product, Category


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedIdentityField(
        many=True, read_only=True, view_name="product-detail")
    
    # category = serializers.HyperlinkedIdentityField(
    #     many=False, read_only=True, view_name="category-detail")

    class Meta:
        model = Category
        fields = "__all__"
