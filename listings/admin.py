from django.contrib import admin
from .models import Listing

# Register your models here. where we can customize admin stuff for the listings app

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('state',)
    list_editable = ('is_published', )
    search_fields = ('title', 'description', 'address', 'city', 'state', 'price')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin) 