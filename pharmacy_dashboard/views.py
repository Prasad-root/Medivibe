from django.shortcuts import render,redirect
from .forms import ProductCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductCreationForm,ProductUpdateForm
from .models import Product
from django.shortcuts import get_object_or_404


def main_view(request):
    return render(request,'main_view.html')

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

@login_required
def update_product(request,product_id):
    queryset = Product.objects.get(product_id = product_id)
    form = ProductUpdateForm(instance=queryset)
    if request.method == "POST":
        form = ProductUpdateForm(request.POST,request.FILES,instance=queryset)
        if form.is_valid():
            form.save()
            return redirect("stores")
        else:
            redirect("stores")
    else:
        return render(request,'product_update.html',{'product_update_form':form,'product_id':product_id})


@login_required
def stores(request):
    queryset = Product.objects.filter(pharmacy=request.user) 
    context = {
        'product_details': queryset
    }
    return render(request, 'stores.html', context)

@login_required
def remove_product(request,product_id):
    item_to_delete = get_object_or_404(Product, product_id=product_id)
    if item_to_delete:
        item_to_delete.delete()
        messages.info(request,"Product Deleted Successfully...")
        return redirect('stores')
    else:
        messages.info(request,"Product Deleting Process Failed...")
        return redirect('product_update')