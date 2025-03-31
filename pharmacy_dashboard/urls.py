from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_view,name = 'main_view'),
    path('/stores',views.stores,name = "stores"),
    path('/product_insert',views.product_insert,name='product_insert'),
    path('/product_details_up/<int:product_id>',views.update_product,name='product_update'),
    path('/remove_product/<int:product_id>',views.remove_product,name='remove_product')
]