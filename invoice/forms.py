import imp
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from . models import Client,Product,Invoice,Setting

class DateInput(forms.DateInput):
    input_type = 'date'

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email','password'
        ]

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'clientName','logo','phone_number','email'
        ]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name','quantity','description','unit_price'
        ]

class InvoiceForm(forms.ModelForm):
    due_date = forms.DateField(
        required=True,
        label='Invoice Due',
        widget=DateInput(attrs={'class':'form-control'}),   
    )
    class Meta:
        model = Invoice
        fields = [
            'invoice_name','due_date','payment_Terms','status','notes','client','product'
        ]
    
class SettingForm(forms.ModelForm):
    class Meta:
        fields = [
            'clientName','logo','phone_number','email'
        ]