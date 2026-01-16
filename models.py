from django.db import models
from customer.models import Customer  # Import the Customer model

class List(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='lists')  # ForeignKey to Customer
    tag_name = models.CharField(max_length=100)  # Tag name for the list

    def __str__(self):
        return f'{self.customer.id} - {self.tag_name}'  # Display customer id and tag name
