# inventory1/models.py
from django.db import models
from customer.models import Customer  # Ensure this points to the correct location

class Inventory(models.Model):
    flat = models.CharField(max_length=100)
    image_name = models.CharField(max_length=255)
    price = models.FloatField()
    address = models.CharField(max_length=255)
    description = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='inventory_items')

    def __str__(self):
        return f"{self.flat} ({self.customer.name})"