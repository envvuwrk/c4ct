from . import views
from django.urls import path



urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('products/', views.products, name='products'),
    path('support/', views.support, name='support'),
    path('clients/',views.clients,name='clients'),
    path('contact/',views.contact,name='contact'),
]
