from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('categories/', views.categories, name='categories'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('accounts/', include('allauth.urls')),
]

from django.contrib import admin
from django.urls import path

urlpatterns = [
    # Outras URLs do seu projeto
    path('admin/', admin.site.urls),
    # Mais URLs do projeto, se houver
]
