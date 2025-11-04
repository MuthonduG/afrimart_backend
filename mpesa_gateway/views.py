from django.shortcuts import render
import requests
import base64
from decouple import config
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serializers import MpesaSerializer

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def initiate_payment(self):
   if not self.user:
      return Response(
         {"error": "user must be logged in"},
         status=status.HTTP_401_UNAUTHORIZED
      )
   
   phone_number = int(user.phone_number)

   request_data = {
      "BusinessShortCode": config('BIZSHORTCODE'),
      "PASSWORD": MpesaSerializer.generate_mpesa_password.decode_pass,
      "Timestamp": MpesaSerializer.generate_mpesa_password.paid_at,
      "TransactioType": "CustomerPayBillOnline",
      "PartyA": config("PARTY_A"),
      "PartyB": config("PARTY_B"),
      "PhoneNumber": phone_number,
      "CallbackURL": config("CALLBACK_URL"),
      "AccountRefernce": config("ACCOUNT_REFERENCE"),
      "TransactionType": config("TRANSACTION_DESC")
   }
   pass

