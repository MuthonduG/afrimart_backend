from django.db import models
from djongo import models as djongo_models
from django.core.validators import MinLengthValidator
from user_auth.models import User
from product.models import Product

class Order(models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True, editable=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')

    address_line_one = models.CharField(max_length=256, validators=[MinLengthValidator(4)])
    address_line_two = models.CharField(max_length=256, validators=[MinLengthValidator(4)])
    city = models.CharField(max_length=256, validators=[MinLengthValidator(4)])
    country = models.CharField(max_length=256, validators=[MinLengthValidator(3)])
    postal_code = models.CharField(max_length=10)

    status = models.CharField(max_length=10, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {_id}"
