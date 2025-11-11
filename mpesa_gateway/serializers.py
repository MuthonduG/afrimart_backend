from rest_framework import serializers
from .models import Mpesa
import requests
import base64
from decouple import config
from requests.auth import HTTPBasicAuth
from datetime import datetime


class MpesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mpesa
        fields = ['id', 'paid_at', 'amount']

    def generate_access_token(self):
        consumer_key = config('CONSUMER_KEY')
        consumer_secret = config('CONSUMER_SECRET')
        token_url = config('BASEURL')

        response = requests.get(
            token_url,
            auth=HTTPBasicAuth(consumer_key, consumer_secret)
        ).json()

        return response['access_token']

    def generate_password(self):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        shortcode = config("BIZSHORTCODE")
        passkey = config("PASSKEY")

        data = shortcode + passkey + timestamp
        encoded = base64.b64encode(data.encode()).decode('utf-8')

        return encoded, timestamp
      