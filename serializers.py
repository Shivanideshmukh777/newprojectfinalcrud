from rest_framework import serializers
from .models import Lead, Customer  # Import both models

class LeadSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=15)
    email = serializers.EmailField()
    summary = serializers.CharField()
    status = serializers.ChoiceField(choices=Lead.STATUS_CHOICES)
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())  # Linking to Customer model
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Lead
        fields = ['name', 'phone', 'email', 'summary', 'status', 'customer', 'created_at']
        read_only_fields = ['created_at']
