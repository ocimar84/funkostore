from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def product_view(request):
    return render(request, 'product.html')
