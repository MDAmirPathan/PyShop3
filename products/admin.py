from django.contrib import admin
from .models import Product, Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProdcutAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProdcutAdmin)