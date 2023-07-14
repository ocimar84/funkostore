from django.contrib import admin
from django.urls import path
from . import views
from .views import products


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
]
