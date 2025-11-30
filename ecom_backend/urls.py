from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/user/api/', include('user_auth.urls')),
    path('product/api/', include('product.urls')),
    path('mpesa/api/', include('mpesa_gateway.urls')),
    path('order/api/', include('order.urls'))
]
