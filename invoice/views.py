from itertools import count
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .forms import *
from .models import Product,Client,Invoice
from uuid import uuid4

# Create your views here.
def index(request):
    clients = Client.objects.all()
    count = Client.objects.all()
    context={
        'clients':clients,
        'count' :count
    }
    return render(request,'invoice/index.html',context)

def base(request):
    clients = Client.objects.all()
    count = Client.objects.all()
    context={
        'clients':clients,
        'count' :count
    }
    return render(request,'base.html',context)
def create_invoice(request):
    context={

    }
    return render (request,'invoice/create_invoice.html',context)


@login_required
def invoices(request):
    
    invoices = Invoice.objects.all()
    context = {
        'invoices':invoices
    }
    return render(request, 'invoice/invoices.html', context)


@login_required
def products(request):
    context = {
        'products':products
    }
    products = Product.objects.all()
    return render(request, 'invoice/products.html', context)

def createClient(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients')
    context = {
        'form':form
    }
    return render (request,'invoice/client_form.html',context)

def clients(request):
    context = {}
    clients = Client.objects.all()
    context['clients'] = clients

    if request.method == 'GET':
        form = ClientForm()
        context['form'] = form
        return render(request, 'invoice/clients.html', context)

    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, 'New Client Added')
            return redirect('clients')
        else:
            messages.error(request, 'Problem processing your request')
            return redirect('clients')


    return render(request, 'invoice/clients.html', context)



    # ---------------------------------invoices ---------------------------------------------#
@login_required
def createInvoice(request):
    # create a blank invoice...
    number = 'INV-'+str(uuid4()).split('-')[1]
    newInv = Invoice.objects.create(number=number)
    newInv.save()

    # fetch invoice
    inv = Invoice.objects.get(number=number)
    products = Product.objects.filter(invoice=invoice)
    products  = Product.objects.all()
    context = {
        'inv':inv,
        'products':products,
    }
    

    if request.method == 'GET':
        prod_form = ProductForm()
        inv_form = InvoiceForm(instance=invoices)

        context = {
            'prod_form':prod_form,
            'inv_form':inv_form
        }
        return render(request, 'invoice/create-invoice.html',context)

    
    return render(request, 'invoice/create-invoice.html',context)

    
