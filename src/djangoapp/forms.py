from django import forms
from .models import Item, Price
import random
import string


class ItemsForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_id', 'model_no', 'make', 'description']


class PricesForm(forms.ModelForm):
    class Meta:
        model = Price
        #item_id = Item.item_id
        fields = ['item_id', 'cost', 'sell']
