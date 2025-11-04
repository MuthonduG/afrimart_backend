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
        fields = [
            'id', 'paid_at', 'amount', 'user[phone_number]'
        ]
    
    def generate_access_token():
        consumer_key = config('CONSUMER_KEY')
        consumer_secret = config('CONSUMER_SECRET')
        base_url = config('BASEURL')

        m_token = requests.get(
            base_url,
            auth= HTTPBasicAuth(consumer_key, consumer_secret)
        ).json()
        
        res = json.dumps(m_token, indent=4)
        validaed_token = m_token['access_token']

    def generate_mpesa_password():
        paid_at = datetime.now().strftime('%Y%m%d%H%M%S')
        biz_shortcode = config('BIZSHORTCODE')
        offset_value = '0'
        pass_key = config('PASSKEY')

        data_to_encode = biz_shortcode + pass_key + paid_at

        encode_pass = base64.b64encode(data_to_encode.encode())
        decode_pass = encode_pass.decode('utf-8')

        

    

        


