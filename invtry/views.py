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
class ItemViewSet(viewsets.ViewSet):
    queryset = Item.objects.all().order_by('-id')
    serializer = ItemSerializer(queryset, many=True)

    
    # def list(self, request):
    #     queryset = Item.objects.all().order_by('-id')
    #     serializer = ItemSerializer(queryset, many=True)
    #     return Response(serializer.data)
    
    # def retrieve(self, request, pk=None):
    #     queryset = Item.objects.all()