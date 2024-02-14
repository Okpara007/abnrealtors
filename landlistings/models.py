from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField

class LandListing(models.Model):
    title = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    price = models.IntegerField(blank=True)
    sqm = models.IntegerField(blank=True, default=0)
    lot_size = models.DecimalField(max_digits=5, decimal_places=1, blank=True)
    description = models.TextField(blank=True)
    list_date = models.DateField(default=datetime.now, blank=True)
    photo_main = CloudinaryField('image', blank=True)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title