from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    
    path('create_invoice/',views.create_invoice,name='create_invoice'),
]