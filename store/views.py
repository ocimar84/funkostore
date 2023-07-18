from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def products(request):
    return render(request, 'product.html')

def categories(request):
    return render(request, 'categories.html')
