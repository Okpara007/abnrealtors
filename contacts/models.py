from django.db import models
from datetime import datetime

class Contact(models.Model):
    listing = models.CharField(max_length=200, null=True)  # Existing fields remain unchanged
    listing_id = models.IntegerField(null=True)  # Can refer to property listing
    landlisting_id = models.IntegerField(null=True)  # New field for land listing reference
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    message = models.TextField(blank=True, null=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
