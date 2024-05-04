from django.template.defaultfilters import default
from rest_framework import serializers
from .models import Product, Category


class СartSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    override = serializers.BooleanField(default=False)


class СartDetailSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    override = serializers.BooleanField(default=True)


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for  Product"""
    category = serializers.SlugRelatedField(many=False, read_only=True, slug_field="slug")

    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Category"""
    # products = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name="product-detail")
    products = serializers.SlugRelatedField(many=True, read_only=True, slug_field="slug")

    class Meta:
        model = Category
        fields = "__all__"


class ProductPostSerializer(serializers.Serializer):
    """Serializer for  Product if you want use POST method """
    categories = Category.objects.all()
    id = serializers.IntegerField(read_only=True)
    category = serializers.ChoiceField(choices=[cat.name for cat in categories])
