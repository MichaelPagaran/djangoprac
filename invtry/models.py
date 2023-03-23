from django.db import models

# Create your models here.

class Item(models.Model):
    description = models.CharField(max_length=200)
    value = models.IntegerField(default=0)