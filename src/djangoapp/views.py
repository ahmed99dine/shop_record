from django.shortcuts import render, redirect
from .forms import ItemsForm, PricesForm
from .models import Item, Price
from pprint import pprint

# Create your views here.


def home(request):
    title = "Welcome: This is the home page "
    context = {
        "title": title,
    }
    return render(request, "home.html", context)


def item_entry(request):
    title = "Add Item"

    form = ItemsForm(request.POST or None)
    # price_form = PricesForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "title": title,
        "form": form,  # "price_form": price_form
    }
    return render(request, "item_entry.html", context)


def price_entry(request):
    title = "Add Price"

    item = Item.objects.get(pk=request.GET['item_id'])
    initial_dict = {"item_id": item}
    form = PricesForm(request.POST or None, initial=initial_dict)
    if form.is_valid():
        form.save()
    context = {
        "title": title,
        "form": form,
        "item": item,
    }
    return render(request, "price_entry.html", context)


def item_list(request):
    title = 'List of items'
    queryset = Item.objects.all()
    #gross_margin =  Price.objects.raw('SELECT *,((sell-cost)/self) AS gross_margin FROM djangoapp_price')

    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "item_list.html", context)


def price_list(request):
    title = 'Price List'
    queryset = Price.objects.all()  # Item.objects.all()
    context = {
        "title": title,
        "queryset": queryset,

    }
    return render(request, "price_list.html", context)
