"""
URL configuration for notifypro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from customer.views import CustomerAPIView
from lead.views import LeadAPIView
from inventory.views import InventoryAPIView
from list.views import ListAPIView
from user.views import UserAPIView, LoginAPI

def api_root(request):
    return render(request, 'index.html')

def favicon_view(request):
    from django.http import HttpResponse
    return HttpResponse(status=204)  # Empty response to eliminate 404

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', api_root),
    path('favicon.ico', favicon_view),
    path('customer/', CustomerAPIView.as_view()),
    path('lead/', LeadAPIView.as_view()),  
    path('inventory/', InventoryAPIView.as_view()),  
    path('list/', ListAPIView.as_view()), 
    path('user/', UserAPIView.as_view()), 
    path('login/', LoginAPI.as_view()), 
    
    
]

