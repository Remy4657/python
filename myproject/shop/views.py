from django.shortcuts import render
from django.http import HttpResponse
from . models import Products
from . main import lookup_table, ranked_products

# Create your views here.

def index(request):
    list_products = Products.objects.all()
    context = {"list_product": list_products}
    return render(request, 'shop/index.html', context)


def viewdetail(request, request_name):
    p = Products.objects.get(product_name=request_name)
    lq = []
    for item in lookup_table.items():
        if item[0] == p.product_name:
            lq = item[1]
    if len(lq) < 3:
        lq = ranked_products[:3]
    temp = []
    for i in lq:
        a = Products.objects.get(product_name=i)
        temp.append(a)
    return render(request, 'shop/detail_product.html', {"dp": p, "lq": temp})