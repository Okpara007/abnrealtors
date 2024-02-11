from django.contrib import admin
from .models import LandListing

class LandListingAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'is_published', 'city', 'state', 'price', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('city', 'state')
    list_editable = ('is_published', )
    search_fields = ('title', 'description', 'address', 'city', 'state')
    list_per_page = 25

admin.site.register(LandListing, LandListingAdmin)