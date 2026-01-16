from rest_framework import serializers
from .models import List

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['customer', 'tag_name']  # Only include customer ID and tag_name
