from django.urls import path
from . import views

urlpatterns = [
    path('catelog',views.catelog,name = 'catelog'),
    path('product_view/<int:product_id>/',views.product_view,name = 'product_view'),
    path('checkout',views.checkout,name = 'checkout'),
    path('cart',views.cart,name='cart')
]