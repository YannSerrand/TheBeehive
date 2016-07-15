from datetime import date

from django.shortcuts import render, redirect
from django.template import RequestContext 
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from models import *
from form import AccountForm


def index(request):
    
    return render(request, "home.html")

def sales(request):
    
    last_sales = Sale.objects.all().order_by('-date')    
    
    #to add        
    #nb_producers = 
    today = date.today()
    return render(request, "sales.html", {'sales': last_sales, 'today':today})


def sales_detail(request, sale_id):
    
    # to add : test if there is none
    s = Sale.objects.filter(id__exact = sale_id)[0]
    
    producers = ProductPerSale.objects.filter(sale_id__exact = sale_id).values_list('product__producer').distinct()
    
    products = []
    
    for p in producers:
        products.append(ProductPerSale.objects.filter(sale_id__exact = sale_id, product__producer__id = p[0]))
    
    return render(request, "sales_detail.html", {'sale': s, 'products': products})

def cart(request):
    
    if request.user.is_authenticated():
        
        print request.user
        cart = Cart.objects.filter(client__exact = request.user)[0]
        
        total_cost = 0
        for c in cart.cart_content.all():
            total_cost += c.cost 
        print total_cost
        return render(request, "cart.html", {'cart': cart, 'total':total_cost})

    else:
        
        return redirect('/accounts/login')

def producers_list(request):
    
    producers = Producer.objects.all().order_by('-name')
    
    return render(request, "producers.html", {'producers':producers})

def join(request):
    
    if request.method == 'POST':

        form = AccountForm(request.POST)
        
        if form.is_valid():
            
            #create user
            client = User(username = form["username"].value(), first_name = form["first_name"].value(),
                           last_name = form["last_name"].value(), email = form["email"].value(),
                           password = form["password"].value(),
                              is_staff = False, is_active = True, is_superuser = False)
            client.save()
            
            return render(request, "creation_successful.html", {'client':client})
            
    else:
        
        form = AccountForm()
    
    return render(request, "join.html", {'form': form})

def profile(request):
    
    user = request.user
    
    if user.is_authenticated():
        
        return render(request, 'profile.html', {'user': user})
    
    else:
        
        return redirect('/accounts/login')