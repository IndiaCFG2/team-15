from django.contrib import admin
from django.urls import path,include
from django.conf import settings


urlpatterns = [


    path('admin/', admin.site.urls),
    path('urlmagic/',include('urlgen.urls')),
    path('accounts/', include('accounts.urls')),
    path('main/', include('main.urls')),
    path('admins/', include('admins.urls')),

]
