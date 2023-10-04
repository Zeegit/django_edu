from timeit import default_timer

from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.
from django.template.defaulttags import lorem

from .models import Product


def shop_index(request: HttpRequest) -> HttpResponse:
    products = [
        ("Пыво", 2),
        ("Воттка", 4),
        ("Рооом", 6),
    ]
    context = {
        "time_running": default_timer(),
        "products": products
    }

    # return HttpResponse("<h1>Hello</h1>")

def groups_list(request: HttpRequest) -> HttpResponse:
    context = {
        "groups": Group.objects.prefetch_related('permissions').all(),
     }
    return render(request, 'shopapp/groups-list.html', context=context)


def products_list(request: HttpRequest) -> HttpResponse:
    context = {
        "products": Product.objects.all(),
     }
    return render(request, 'shopapp/products-list.html', context=context)