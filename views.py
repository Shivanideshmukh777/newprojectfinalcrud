from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Lead
from .serializers import LeadSerializer


class LeadAPIView(APIView):
    # Create a new lead (POST)
    def post(self, request):
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the lead to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Retrieve leads (GET). If ID is provided, return that specific lead.
    def get(self, request, id=None):
        if id:
            try:
                lead = Lead.objects.get(id=id)  # Retrieve a specific lead
            except Lead.DoesNotExist:
                return Response({"error": "Lead not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = LeadSerializer(lead)
            return Response(serializer.data)
        leads = Lead.objects.all()  # Retrieve all leads
        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data)

    # Update an existing lead (PUT)
    def put(self, request, id):
        try:
            lead = Lead.objects.get(id=id)  # Retrieve the lead to update
        except Lead.DoesNotExist:
            return Response({"error": "Lead not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = LeadSerializer(lead, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the updated lead
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a lead (DELETE)
    def delete(self, request, id):
        try:
            lead = Lead.objects.get(id=id)  # Retrieve the lead to delete
        except Lead.DoesNotExist:
            return Response({"error": "Lead not found"}, status=status.HTTP_404_NOT_FOUND)
        lead.delete()  # Delete the lead
        return Response({"message": "Lead deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
