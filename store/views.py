from django.shortcuts import render
from django.http import HttpResponse

def catelog(request):
    return render(request,'catelog.html')

def product_view(request,product_id):
    context = {
        "product_id":product_id
    }
    return render(request,'product_view.html',context)