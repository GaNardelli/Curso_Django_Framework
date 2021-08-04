from django.contrib import admin

from .models import Product, Client

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'storage')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name','lastName', 'email')

admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)