from django.db import models

# Assuming Customer is defined in the same app.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Lead(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    summary = models.TextField()
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='active')
    
    # String reference to Customer model to avoid circular import
    customer = models.ForeignKey('Customer', related_name='leads', on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
