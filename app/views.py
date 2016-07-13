from django.shortcuts import render
from django.template import RequestContext 
from django.http import HttpResponse

from models import *


def index(request):
    
    return render(request, "home.html")


def sales(request):
    
    last_sales = Sale.objects.all().order_by('-date')    
    
    #to add        
    #nb_producers = 
    
    return render(request, "sales.html", {'sales': last_sales})


def sales_detail(request, sale_id):
    
    # to add : test if there is none
    s = Sale.objects.filter(id__exact = sale_id)[0]
    
    producers = ProductPerSale.objects.filter(sale_id__exact = sale_id).values_list('product__producer').distinct()
    
    products = []
    
    for p in producers:
        print ProductPerSale.objects.filter(sale_id__exact = sale_id, product__producer__id = p[0])
        products.append(ProductPerSale.objects.filter(sale_id__exact = sale_id, product__producer__id = p[0]))
    
    return render(request, "sales_detail.html", {'sale': s, 'products': products})
    
    