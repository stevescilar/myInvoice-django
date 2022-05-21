from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    
    path('create_invoice/',views.create_invoice,name='create_invoice'),
    path('clients/',views.clients, name='clients'),
    path('create_client/', views.createClient, name='create_client'),
]