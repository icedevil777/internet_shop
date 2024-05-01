from rest_framework import serializers

from .models import Product, Category


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    
    products = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name="product-detail")

    class Meta:
        model = Category
        fields = "__all__"


class ProductPostSerializer(serializers.Serializer):
    
    categories = Category.objects.all()   
    id = serializers.IntegerField(read_only=True)
    category = serializers.ChoiceField(choices=[cat.name for cat in categories])

