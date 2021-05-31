from django.shortcuts import render
from .models import Listings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def index(request):
    listings=Listings.objects.all()
    paginator=Paginator(listings, 3)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
    context={
        'listings':paged_listings
    }

    return render(request,'listngs/listings.html',context)
def listing(request,listing_id):
    obj=Listings.objects.get(id=listing_id)
    content={
         'obj':obj
     }

    return render(request,'listngs/listing.html',content)
def search(request):
    return render(request,'listngs/search.html')
