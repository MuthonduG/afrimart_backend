import logging
from bson import ObjectId
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Product
from .serializers import ProductSerializer

logger = logging.getLogger(__name__)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProduct(request, pk):
    try:
        product = Product.objects.get(_id=ObjectId(pk))
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)

    serializer = ProductSerializer(product)
    return Response(serializer.data, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProduct(request):
    user = request.user

    if not hasattr(user, "role") or user.role.lower() != "admin":
        return Response({"message": "Only admin users can create products"}, status=403)

    serializer = ProductSerializer(data=request.data, context={'request': request})

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"product": serializer.data, "message": "Product created successfully!"},
            status=201
        )

    logger.error(serializer.errors)
    return Response(serializer.errors, status=400)
