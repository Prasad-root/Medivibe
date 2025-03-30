from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_view,name = 'main_view'),
    path('/stores',views.stores,name = "stores"),
    path('/product_insert',views.product_insert,name='product_insert')
]