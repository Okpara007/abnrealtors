from django.shortcuts import render
from listings.models import Listing
from listings.choices import state_choices, house_type_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:6]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'house_type_choices': house_type_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')