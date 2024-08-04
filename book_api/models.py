from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length =100)
    page_number = models.IntegerField()
    publis_data =models.DateField()
    stock =models.IntegerField()
    