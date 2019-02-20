from django.db import models

# Create your models here.

class tbl_data(models.Model):
    name=models.CharField(max_length=30,blank=True)
    email=models.EmailField(unique= True)
    mobile =models.CharField(max_length = 11,blank=True)