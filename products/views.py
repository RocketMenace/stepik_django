from django.shortcuts import render, HttpResponse
from .models import Product, ProductCategory


# Create your views here.

def index(request):
    context = {"title": "Test title",
               "username": "Ryan Gosling",
               }
    return render(request, "products/index.html", context=context)


def products(request):
    context = {
        "title": "Store - Каталог",
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all()
    }
    return render(request, "products/products.html", context=context)
