from django.shortcuts import render
from django.http import JsonResponse
from .models import Item
from .serializers import ItemSerializer
from invtry.models import Item
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework import status
from rest_framework import viewsets

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
