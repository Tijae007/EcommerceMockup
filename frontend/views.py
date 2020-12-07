from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

def about(request):
    return render(request, 'frontend/about.html')

def phones(request):
    return render(request, 'frontend/phones.html')

def laptops(request):
    return render(request, 'frontend/laptops.html')

def contact(request):
    return render(request, 'frontend/contact.html')

def shirts(request):
    return render(request, 'frontend/about_detail.html')

def screens(request):
    return render(request, 'frontend/product_detail.html')