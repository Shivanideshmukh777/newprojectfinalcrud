# inventory1/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Inventory
from .serializers import InventorySerializer

class InventoryAPIView(APIView):
    """API endpoint for handling CRUD operations for Inventory"""

    # POST: Create new inventory item
    def post(self, request):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new inventory item to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET: Retrieve one or all inventory items
    def get(self, request, id=None):
        if id:
            try:
                inventory = Inventory.objects.get(id=id)
            except Inventory.DoesNotExist:
                return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = InventorySerializer(inventory)
            return Response(serializer.data)
        
        # Get all inventory items
        inventories = Inventory.objects.all()
        serializer = InventorySerializer(inventories, many=True)
        return Response(serializer.data)

    # PUT: Update an existing inventory item
    def put(self, request, id):
        try:
            inventory = Inventory.objects.get(id=id)
        except Inventory.DoesNotExist:
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = InventorySerializer(inventory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: Delete an existing inventory item
    def delete(self, request, id):
        try:
            inventory = Inventory.objects.get(id=id)
        except Inventory.DoesNotExist:
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        inventory.delete()
        return Response({"message": "Deleted"}, status=status.HTTP_204_NO_CONTENT)