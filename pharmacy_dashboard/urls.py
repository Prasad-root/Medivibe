from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_view,name = 'main_view'),
    path('/drug_insert',views.drug_insert,name = "drug_insert")
]