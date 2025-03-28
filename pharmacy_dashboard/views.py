from django.shortcuts import render

def main_view(request):
    return render(request,'main_view.html')

def drug_insert(request):
    return render(request,'drug_insert.html')

