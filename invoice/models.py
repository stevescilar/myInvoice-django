from distutils.command.build_clib import build_clib
from doctest import BLANKLINE_MARKER
from secrets import choice
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from .utils import invoice_no

# Create your models here.
class Client(models.Model):
    clientName = models.CharField(null=True,blank=True,max_length=200)
    phone_number    = models.CharField(max_length=50,unique=True,null=True)
    email = models.EmailField(max_length=100, unique=True,null=True)
    logo = models.ImageField(blank=True,upload_to = 'brandname')
    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True , null=True)


    def __str__(self):
        return '{} {} {}' . format(self.clientName,self.uniqueId,self.email)
    
    def get_absolute_url(self):
        return reverse ('client-detail', kwargs={'slug':self.slug})

    def save(self,*args,**kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {} {}' . format(self.clientName,self.uniqueId,self.email))

        self.slug = slugify('{} {} {}' . format(self.clientName,self.uniqueId,self.email))
        self.last_updated = timezone.localtime(timezone.now())

        super(Client, self).save(*args, **kwargs)
        
class Product(models.Model):
    name = models.CharField(null=True,blank=True, max_length=100)
    quantity = models.FloatField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    unit_price = models.FloatField(null=True,blank=True)

    # utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True , null=True)

    def __str__(self):
        return '{} {}' . format(self.name, self.uniqueId)
    
    def get_absolute_url(self):
        return reverse ('product-detail', kwargs={'slug':self.slug})

    def save(self,*args,**kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}' . format(self.name, self.uniqueId))

        self.slug = slugify('{} {}' . format(self.name, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Product, self).save(*args, **kwargs)

class Invoice(models.Model):
    TERMS  = [
        ('1 Day','1 Day'),
        ('7 Days','7 Days'),
        ('14 Days','14 Days'),
        ('21 Day','21 Days'),
    ]
    STATUS = [
        ('CURRENT','CURRENT'),
        ('OVERDUE','OVERDUE'),
        ('PAID','PAID'),

    ]

    invoice_name = models.CharField(null=True, blank=True, max_length=100)
    invoice_no = models.CharField(
           max_length = 6,null=True,
           blank=True,
           editable=False,
           unique=True,
           default=invoice_no)
    due_date  = models.DateField(null=True, blank=True)
    payment_Terms = models.CharField(choices=TERMS, default='1 Day',max_length=100)
    status = models.CharField(choices=STATUS,default='CURRENT',max_length=100)
    notes = models.TextField(null=True, blank=True)

    # related fields
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.SET_NULL)

    # utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True , null=True)

    def __str__(self):
        return '{} {}' . format(self.invoice_name, self.uniqueId)
    
    def get_absolute_url(self):
        return reverse ('invoice-detail', kwargs={'slug':self.slug})

    def save(self,*args,**kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}' . format(self.invoice_name, self.uniqueId))

        self.slug = slugify('{} {}' . format(self.invoice_name, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Product, self).save(*args, **kwargs)

class Setting(models.Model):
    clientName = models.CharField(null=True,blank=True,max_length=200)
    phone_number    = models.CharField(max_length=50,unique=True,null=True)
    email = models.EmailField(max_length=100, unique=True,null=True)
    logo = models.ImageField(blank=True,upload_to = 'brandname')
    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True , null=True)


    def __str__(self):
        return '{} {} {}' . format(self.clientName,self.uniqueId,self.email)
    
    def get_absolute_url(self):
        return reverse ('client-detail', kwargs={'slug':self.slug})

    def save(self,*args,**kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {} {}' . format(self.clientName,self.uniqueId,self.email))

        self.slug = slugify('{} {} {}' . format(self.clientName,self.uniqueId,self.email))
        self.last_updated = timezone.localtime(timezone.now())

        super(Setting, self).save(*args, **kwargs)
        