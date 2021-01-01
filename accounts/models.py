from django.db import models

# Create your models here.
from django.contrib.auth.models import User  
  
class Category(models.Model):
    date = models.DateField()
    
    
    def __str__(self):
        return self.date
class Item(models.Model):
    STATUS_CHOICES=(("PENDING","Pending"),("NOT AVAILABLE","Not Available"),("BOUGHT","Bought"))
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    status = models.CharField(max_length=20,
                  choices=STATUS_CHOICES,
                  default="PENDING")
    added_date = models.DateField()
    buyer = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    #cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name  
    
