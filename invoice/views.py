from django.shortcuts import render

# Create your views here.
def index(request):
    context={

    }
    return render(request,'invoice/index.html',context)

def create_invoice(request):
    context={

    }
    return render (request,'invoice/create_invoice.html',context)