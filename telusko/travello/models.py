from django.db import models

# Create your models here.
class Destination(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField( max_length=50)
    desc = models.TextField()
    img = models.ImageField( upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(("False"))
    
