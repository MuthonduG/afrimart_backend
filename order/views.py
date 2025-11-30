from bson import ObjectId
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Order
from .serializers import OrderSerializer
from product.models import Product


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    product_id = request.data.get("product_id")

    if not product_id:
        return Response({"error": "product_id is required"}, status=400)

    try:
        product = Product.objects.get(_id=ObjectId(product_id))
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)

    serializer = OrderSerializer(data=request.data, context={'request': request})

    if serializer.is_valid():
        order = serializer.save()
        return Response(
            {"message": "Order created successfully", "order": OrderSerializer(order).data},
            status=201
        )

    return Response(serializer.errors, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_order_status(request):
    user = request.user

    if not hasattr(user, "role") or user.role.lower() != "admin":
        return Response({"error": "Only admins can update orders"}, status=403)

    order_id = request.data.get("order_id")
    new_status = request.data.get("status")

    if not order_id or not new_status:
        return Response({"error": "order_id and status are required"}, status=400)

    try:
        order = Order.objects.get(_id=ObjectId(order_id))
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=404)

    serializer = OrderSerializer(order, data={"status": new_status}, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Order updated successfully", "order": serializer.data},
            status=200
        )

    return Response(serializer.errors, status=400)

