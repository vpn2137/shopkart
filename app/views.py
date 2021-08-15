from django.shortcuts import render

from store.models import Product


def home(request):
    products = Product.objects.all().filter(is_avilabel=True)
    contex={
        'products': products,
    }
    return render(request, 'home.html', contex)