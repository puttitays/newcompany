from django.contrib import admin

from.models import *

# Register your models here.

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('img','Type','Color','user','product_name', 'Width', 'Height', 'Quantity', 'Price','total','Name','Phone','Street','PostalCode','City','Note','Payment_received')

class Order_from_offerAdmin(admin.ModelAdmin):
    list_display=("user_name","Telephone","Email","Order")

admin.site.register(Orders,OrdersAdmin)

admin.site.register(Order_from_offer,Order_from_offerAdmin)

