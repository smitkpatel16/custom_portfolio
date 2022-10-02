from django.shortcuts import render
from .models import Image
# Create your views here.


def home(request):
    return render(request, 'index.html')


def portfolio(request):
    images = Image.objects.all()
    context = {"uploadlist": images,
               "categoryList": list(set(i.category for i in images))}
    return render(request, 'portfolio.html', context)
