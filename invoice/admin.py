from django.contrib import admin

from invoice.utils import invoice_no
from . models import Client,Product,Invoice,Setting


class ClientAdmin(admin.ModelAdmin):
    list_display = ('clientName','phone_number','email','uniqueId','slug','date_created','last_updated')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','quantity','unit_price','description','slug','date_created','last_updated')

admin.site.register(Client,ClientAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Invoice)
admin.site.register(Setting)
