from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator 
from django.conf import settings
import uuid



class User(AbstractUser):
    Name = models.CharField(max_length=200)
    Budget = models.FloatField(blank=True, null=True)

class Stock_item(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='owned_stock_items'
    )
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=500)
    in_stock = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])
    Buy_Price = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])
    Sell_Price = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    img = models.ImageField(upload_to='items_img/',blank=True, null=True)

    def __str__(self):
        return f"{self.Name} {self.in_stock}"



class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    
    # Point to the WHOLE model 'Stock_item', not a specific field
    item = models.ForeignKey('Stock_item', on_delete=models.PROTECT)
    
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    buy = models.BooleanField(null=True, blank=True)
    def __str__(self):
        return f"{self.item}   {self.timestamp} "
