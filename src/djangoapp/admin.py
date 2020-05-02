from django.contrib import admin
from .models import Item, Price
from .forms import ItemsForm, PricesForm
# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_id', 'model_no', 'make', 'description']
    form = ItemsForm
    list_filter = ['make', 'description']
    search_fields = ['item_id', 'model_no', 'make', 'description']


class PriceAdmin(admin.ModelAdmin):
    list_display = ['item_id',  'cost', 'sell']
    form = PricesForm
    #list_filter = ['item_id', 'cost', 'rrp']
    search_fields = ['item_id', 'cost', 'sell']


admin.site.register(Item, ItemAdmin)
admin.site.register(Price, PriceAdmin)
