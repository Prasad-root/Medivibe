from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('main_site.urls')),
    path('authentication/',include('authentication.urls')),
    path('pharmacy_view',include('pharmacy_dashboard.urls')),
    path('store/',include('store.urls'))
]


