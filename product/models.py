from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from user_auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    product_name = models.CharField( max_length=256 ,validators=[MinLengthValidator(10)])
    product_description = models.TextField(max_length=256, validators=[MinLengthValidator(30)])
    product_price = models.CharField(max_length=6)
    discount_percentage = models.IntegerField( validators=[MinValueValidator(0), MaxValueValidator(100)], default=0,help_text="Discount percentage (0-100)")
    product_brand = models.CharField(max_length=100)
    product_category = models.CharField(max_length=100)
    product_qty = models.IntegerField(default=0)
    product_image_url = models.CharField(max_length=256, null=True, blank=True)
    product_rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    product_features = models.ArrayField(models.CharField(max_length=200), blank=True, default=list)
    product_specifications = models.DictField( blank=True, default=dict)
    product_colors = models.ArrayField( models.CharField(max_length=50), blank=True, default=list )
    product_warranty = models.DictField( default=dict, blank=True )
    deal_tag = models.CharField(
        max_length=50, 
        blank=True, 
        null=True, 
        choices=[
            ('Flash', 'Flash Sale'),
            ('Clearance', 'Clearance'),
            ('Deal', 'Special Deal'),
            ('Bundle', 'Bundle Offer'),
        ],
        help_text="Type of deal if applicable"
    )
    is_new = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.product_title