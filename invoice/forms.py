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
    logo = forms.ImageField(required=False, error_messages={'invalid':("image files only")}, widget=forms.FileInput)
    class Meta:
        model = Client
        fields = [
            'clientName','logo','phone_number','email','company_name'
        ]
# class="input-group input-group-outline my-3"
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['clientName'].widget.attrs['placeholder'] = 'Enter client Names'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter client Email Address'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter client Phone Number'
        self.fields['company_name'].widget.attrs['placeholder'] = 'Enter client company name'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name','quantity','description','unit_price','invoices'
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
            'invoice_name','due_date','payment_Terms','status','notes'
        ]
    
class SettingForm(forms.ModelForm):
    class Meta:
        fields = [
            'clientName','logo','phone_number','email'
        ]