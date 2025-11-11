from django.urls import path
from .views import initiate_payment, mpesa_callback

urlpatterns = [
    path('initiate_payment/', initiate_payment, name='initiate_payment'),
    path('mpesa_callback/', mpesa_callback, name='mpesa_callback'),
]