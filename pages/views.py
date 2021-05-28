from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listings
from realtors.models import Realtor

# Create your views here.
def index(request):
    list=Listings.objects.order_by('-list_date').filter(is_published=True)[:3]
    content={
        'liste':list
    }
    return  render(request,'pages/index.html',content)
def about(request):
     realtor=Realtor.objects.all()
     mvp=Realtor.objects.all().filter(is_mvp=True)
     content={
         'lists':realtor,
         'ismvp':mvp
     }

     return render(request,'pages/About.html',content)