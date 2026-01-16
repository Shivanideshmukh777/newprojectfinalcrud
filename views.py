from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializer import UserSerializer, LoginSerializer

# Create your views here.

class LoginAPI(APIView):
    """API endpoint for user login"""
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            try:
                user = User.objects.get(email=email,password=password)
            except User.DoesNotExist:
                return Response(
                    {"message": "Invalid email or password"}, 
                    status=status.HTTP_401_UNAUTHORIZED
                )
            
            # Check password
            if user:
                return Response({
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "message": "Login successful"
                }, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"message": "Invalid email or password1"}, 
                    status=status.HTTP_401_UNAUTHORIZED
                )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAPIView(APIView):
    def post(self,request):
        
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,id=None):
        if id:
            try:
                user= User.objects.get(id=id)
            except User.DoesNotExist:
                return Response({"error":"Not Found"},status=status.HTTP_404_NOT_FOUND)
            
            serializer = UserSerializer(user)
            return Response(serializer.data)
        users =User.objects.all()
        serializer =UserSerializer(users, many = True)
        return Response(serializer.data)

    def put(self,request,id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"error":"Not Found"},status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"error":"Not Found"},status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response({"message":"Deleted"},status=status.HTTP_204_NO_CONTENT)

# class LoginAPI(APIView):
#     """API endpoint for user login"""

#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
        
#         if serializer.is_valid():
#             email = serializer.validated_data['email']
#             password = serializer.validated_data['password']
            
#             # Authenticate user
#             user = authenticate(request, username=email, password=password)
            
#             if user is not None:
#                 return Response({
#                     "id": user.id,
#                     "name": user.name,
#                     "email": user.email,
#                     "message": "Login successful"
#                 }, status=status.HTTP_200_OK)
#             else:
#                 return Response(
#                     {"message": "Invalid email or password"}, 
#                     status=status.HTTP_401_UNAUTHORIZED
#                 )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
