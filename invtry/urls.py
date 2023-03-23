from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('list/', views.item_list),
    path('list/<int:id>', views.item_detail),
]