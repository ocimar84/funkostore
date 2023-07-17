from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def products(request):
    return render(request, 'myapp/product.html')

def categories(request):
    return render(request, 'myapp/categories.html')
