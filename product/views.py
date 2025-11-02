import logging
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer

logger = logging.getLogger(__name__)

# Get all products
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Get product by id
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProduct(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Create product
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProduct(request):
    product_title = request.data.get('product_title')
    product_description = request.data.get('product_description')
    product_price = request.data.get('product_price')
    
    if not product_description or not product_price or not product_title:
        return Response(
            {'error': 'All fields are required'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "product": serializer.data,
                "message": "Product created successfully!"
            },
            status=status.HTTP_201_CREATED
        )

    logger.error(f"Product creation errors: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
