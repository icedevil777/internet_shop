from django.template.defaultfilters import default
from rest_framework import serializers
from .models import Order, OrderItem, Product, Category


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields: str = "__all__"

    def create(self, validated_data) -> Order:
        return Order.objects.create(**validated_data)


class СartSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    override = serializers.BooleanField(default=False)


class СartDetailSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    override = serializers.BooleanField(default=True)


class CreateProductSerializer(serializers.ModelSerializer):
    """Serializer for  Product"""
    # category = serializers.SlugRelatedField(many=False, read_only=True, slug_field="slug")

    class Meta:
        model = Product
        fields: str = "__all__"


class ProductSerializer(CreateProductSerializer):
    category = serializers.SlugRelatedField(many=False, read_only=True, slug_field="slug")


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Category"""
    # products = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name="product-detail")
    products = serializers.SlugRelatedField(many=True, read_only=True, slug_field="slug")

    class Meta:
        model = Category
        fields: str = "__all__"


class ProductPostSerializer(serializers.Serializer):
    """Serializer for  Product if you want use POST method """

    try:
        categories = Category.objects.all()
        choices = [cat.name for cat in categories]
    except:
        choices = []

    id = serializers.IntegerField(read_only=True)
    category = serializers.ChoiceField(choices=choices)
