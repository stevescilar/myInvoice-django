from distutils.command.upload import upload
from operator import truediv
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4

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