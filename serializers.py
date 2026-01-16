# inventory1/serializers.py
from rest_framework import serializers
from .models import Inventory
from customer.models import Customer  # Ensure the import path is correct

class InventorySerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), source='customer')

    class Meta:
        model = Inventory
        fields = ['id', 'flat', 'image_name', 'price', 'address', 'description', 'customer_id']