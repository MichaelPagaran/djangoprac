from django.db import models

# Create your models here.

class Item(models.Model):
    # id=models.IntegerField(primary_key=True)
    description = models.CharField(max_length=200)
    value = models.IntegerField(default=0)