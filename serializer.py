from rest_framework import serializers
from.models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length =100)
    email=serializers.EmailField()
    phone=serializers.CharField(max_length =10)
    
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True} 
        }


class LoginSerializer(serializers.Serializer):
    """Serializer for login endpoint"""
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)