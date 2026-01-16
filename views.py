from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import List
from .serializers import ListSerializer

class ListAPIView(APIView):
    
    def post(self, request):
        """Create a new List entry"""
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id=None):
        """Get List entries, either all or a specific one"""
        if id:
            try:
                list_item = List.objects.get(id=id)
            except List.DoesNotExist:
                return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = ListSerializer(list_item)
            return Response(serializer.data)

        lists = List.objects.all()
        serializer = ListSerializer(lists, many=True)
        return Response(serializer.data)

    def put(self, request, id):
        """Update an existing List entry"""
        try:
            list_item = List.objects.get(id=id)
        except List.DoesNotExist:
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ListSerializer(list_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """Delete a List entry"""
        try:
            list_item = List.objects.get(id=id)
        except List.DoesNotExist:
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        list_item.delete()
        return Response({"message": "Deleted"}, status=status.HTTP_204_NO_CONTENT)
