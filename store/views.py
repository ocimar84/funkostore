from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def products(request):
    return render(request, 'product.html')

def categories(request):
    return render(request, 'categories.html')

def contact(request):
    # Your view logic goes here
    return render(request, 'contact.html')

def login(request):
    # Your view logic goes here
    return render(request, 'login.html')