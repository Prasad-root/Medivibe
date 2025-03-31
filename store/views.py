from django.shortcuts import render
from django.http import HttpResponse

def catelog(request):
    return render(request,'catelog.html')

def product_view(request,product_id):
    context = {
        "product_id":product_id
    }
    return render(request,'product_view.html',context)

def checkout(request):
    return render(request,'checkout.html')

def cart(request):
    return render(request,'cart.html')