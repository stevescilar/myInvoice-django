from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'invoice/index.html')

def create_invoice(request):
    return render (request,'invoice/create_invoice.html')