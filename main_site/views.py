from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from authentication.models import Profile

def home(request):
    return render(request,"index.html")

def drug_service(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "drug_search.html")

def prescription_reader(request):
    pass

def pharmacy_rec(request):
    return render(request,"pharmacy_rec.html")


def pharmacy_rec(request):
    staff_users = User.objects.filter(is_staff=True)  # Get all users with is_staff=True
    pharmacies = Profile.objects.filter(user__in=staff_users)  # Get profiles linked to staff users
    return render(request, "pharmacy_rec.html", {'pharmacies': pharmacies})

