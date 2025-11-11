from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Product(models.Model):
    product_title = models.CharField(validators=[MinLengthValidator(10)])
    product_description = models.TextField(validators=[MinLengthValidator(30)])
    product_price = models.FloatField()
    product_image_url = models.CharField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.product_title
