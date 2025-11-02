from django.urls import path
from .views import getProducts, getProduct, createProduct

urlpatterns = [
    path('get_products/', getProducts, name='get_products'),         
    path('get_product/<int:pk>/', getProduct, name='get_product'),  
    path('create_product/', createProduct, name='create_product'),  
]
