from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=10)
    address = serializers.CharField()
    created_at = serializers.DateTimeField()
    password = serializers.CharField(write_only=True)  # Ensure password is not shown in response

    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address', 'created_at', 'password']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        """Override to hash the password before saving"""
        password = validated_data.pop('password')
        customer = Customer(**validated_data)
        customer.set_password(password)
        customer.save()
        return customer
