from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("drug_service",views.drug_service,name = "drug_service"),
    path("prescription_reader",views.prescription_reader,name = "prescription_reader")
]