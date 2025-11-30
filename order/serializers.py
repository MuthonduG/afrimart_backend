from rest_framework import serializers
from bson import ObjectId
from .models import Order
from product.models import Product


class OrderSerializer(serializers.ModelSerializer):
    product_id = serializers.CharField(write_only=True)
    _id = serializers.CharField(read_only=True)   # <── convert to string
    product = serializers.SerializerMethodField()  # <── ensure product shows ObjectId as string

    class Meta:
        model = Order
        fields = [
            '_id',
            'user',
            'product',
            'product_id',
            'address_line_one',
            'address_line_two',
            'city',
            'country',
            'postal_code',
            'status',
            'created_at'
        ]
        read_only_fields = ['user', 'product', 'created_at']

    def get_product(self, obj):
        """Return product as string id instead of ObjectId"""
        return str(obj.product._id)

    def to_representation(self, instance):
        """Ensures all ObjectId fields are converted to strings"""
        rep = super().to_representation(instance)

        # convert order _id (ObjectId -> string)
        rep["_id"] = str(instance._id)

        # convert user id
        rep["user"] = instance.user.id

        # convert product id
        rep["product"] = str(instance.product._id)

        return rep

    def create(self, validated_data):
        product_id = validated_data.pop("product_id")

        try:
            product = Product.objects.get(_id=ObjectId(product_id))
        except Product.DoesNotExist:
            raise serializers.ValidationError({"product_id": "Product not found"})

        validated_data["product"] = product
        validated_data["user"] = self.context["request"].user

        return super().create(validated_data)

    def validate_status(self, value):
        allowed = ["pending", "completed", "cancelled"]
        if value.lower() not in allowed:
            raise serializers.ValidationError(f"Status must be one of: {allowed}")
        return value.lower()
