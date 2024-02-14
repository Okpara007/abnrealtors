from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField

class Listing(models.Model):
    title = models.CharField(max_length=200, blank=True)
    house_type = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=True)
    bedrooms = models.IntegerField(blank=True)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, blank=True)
    sqm = models.IntegerField(blank=True, default=0)
    lot_size = models.DecimalField(max_digits=5, decimal_places=1, blank=True)
    photo_main = CloudinaryField('image', blank=True)
    photo_1 = CloudinaryField('image', blank=True)
    photo_2 = CloudinaryField('image', blank=True)
    photo_3 = CloudinaryField('image', blank=True)
    photo_4 = CloudinaryField('image', blank=True)
    photo_5 = CloudinaryField('image', blank=True)
    photo_6 = CloudinaryField('image', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title


