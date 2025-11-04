from django.db import models
from user_auth.models import User
from product.models import Product


class Mpesa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mpesa_payments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='mpesa_payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.transaction_id} by {self.user.username} for {self.product.product_title}"
