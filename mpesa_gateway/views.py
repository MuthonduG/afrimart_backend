from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from decouple import config
import requests
from .serializers import MpesaSerializer
from product.models import Product


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def initiate_payment(request):
    user = request.user
    product = Product.objects.filter(id=request.get('product_id'))

    amount = product.product_price

    if not amount:
        return Response(
         {"error": "amount is required"}, 
         status=status.HTTP_400_BAD_REQUEST
        )

    phone_number = user.phone_number

    serializer = MpesaSerializer()

    try:
        token = serializer.generate_access_token()
        password, timestamp = serializer.generate_password()
    except Exception:
        return Response(
            {"error": "Failed to generate access token or password"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    stk_push_url = config("STK_PUSH_API")

    request_data = {
        "BusinessShortCode": config("BIZSHORTCODE"),
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": config("BIZSHORTCODE"),
        "PhoneNumber": phone_number,
        "CallBackURL": config("CALLBACK_URL"),
        "AccountReference": "Order Payment",
        "TransactionDesc": "Payment"
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(stk_push_url, json=request_data, headers=headers)
        return Response(response.json(), status=response.status_code)
    except Exception:
        return Response(
            {"error": "Failed to initiate payment"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
