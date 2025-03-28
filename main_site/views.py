from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"index.html")

def drug_service(request):
    return render(request,"drug_search.html")

def prescription_reader(reqest):
    pass