from django.shortcuts import render,redirect
from .forms import ProductCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductCreationForm


def main_view(request):
    return render(request,'main_view.html')

@login_required
def stores(request):
    return render(request,'stores.html')

@login_required
def product_insert(request):
    product_creation_form = ProductCreationForm()
    if request.method == "POST":
        product_create_form_submitted = ProductCreationForm(request.POST, request.FILES)
        if product_create_form_submitted.is_valid():
            user = request.user if request.user.is_authenticated else None
            product_create_form_submitted.save(user=user)
            messages.info(request,"Product Added Successfully...")
            return redirect('product_insert')
        else:
            messages.info(request,product_create_form_submitted.errors)
            return redirect('product_insert')
    else:
        return render(request, "product_insert.html", {'product_creation_form': product_creation_form})

