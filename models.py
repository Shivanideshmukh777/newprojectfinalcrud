from django.db import models
from django.contrib.auth.models import User  # For password handling

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically sets the creation date/time
    password = models.CharField(max_length=255)  # Storing the password hash (recommended)

    def set_password(self, raw_password):
        """Sets the password as a hashed value"""
        self.password = make_random_password()  # You can use Django's built-in password hashers

    def check_password(self, raw_password):
        """Check if the given password matches the stored hashed password"""
        return self.password == raw_password

    def __str__(self):
        return self.name