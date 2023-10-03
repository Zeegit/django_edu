from timeit import default_timer

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.
from django.template.defaulttags import lorem


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
    return render(request, 'shopapp/shop-index.html', context=context)
    # return HttpResponse("<h1>Hello</h1>")
