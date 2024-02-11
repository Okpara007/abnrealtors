from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator 
from .models import LandListing

def index(request):
    landlistings = LandListing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(landlistings, 6)
    page = request.GET.get('page')
    paged_landlistings = paginator.get_page(page)

    context = {
        'landlistings': paged_landlistings
    }
    return render(request, 'landlistings/landlistings.html', context)

def landlisting(request, landlisting_id):
    landlisting = get_object_or_404(LandListing, pk=landlisting_id)
    context = {
        'landlisting': landlisting
    }
    return render(request, 'landlistings/landlisting.html', context)
