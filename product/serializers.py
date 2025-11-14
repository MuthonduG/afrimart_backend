from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 
            'user',
            'product_name', 
            'product_description', 
            'product_price', 
            'discount_percentage',
            'product_brand',
            'product_category',
            'product_qty',
            'product_image_url',
            'product_rating',
            'product_features',
            'product_specifications',
            'product_colors',
            'product_warranty',
            'deal_tag',
            'is_new',
            'date_created'
        ]
        read_only_fields = ['user', 'date_created'] 

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)