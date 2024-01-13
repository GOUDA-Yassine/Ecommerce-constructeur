from django.db import models

# Create your models here.

class Categories(models.Model):
    category = models.CharField( max_length=50)
    
    def __str__(self) :
        return self.category
   
class Product(models.Model):
    name = models.CharField(max_length=100)
    min_decription = models.CharField(max_length=255)
    max_description =  models.TextField()
    price = models.FloatField()
    category = models.ForeignKey("Categories", on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.name
    
    