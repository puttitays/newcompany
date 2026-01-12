from django.contrib import admin
from .models import Product, Offer

# Register your models here.
admin.site.register(Product)


@admin.register(Offer)

class OfferAdmin(admin.ModelAdmin):
     list_display=('name','offer')
     list_editable =('offer',)
     list_display_links = None