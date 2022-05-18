from django.contrib import admin
from . models import Client,Product


class ClientAdmin(admin.ModelAdmin):
    list_display = ('clientName','phone_number','email','uniqueId','slug','date_created','last_updated')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','quantity','unit_price','description','slug','date_created','last_updated')

admin.site.register(Client,ClientAdmin)
admin.site.register(Product,ProductAdmin)
