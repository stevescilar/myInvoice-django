from django.contrib import admin
from . models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('clientName','phone_number','email','uniqueId','slug','date_created','last_updated')
   

admin.site.register(Client,ClientAdmin)
# Register your models here.
