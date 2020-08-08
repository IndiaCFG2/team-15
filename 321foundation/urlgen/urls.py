from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('result/',views.result,name="urlresult"),
    path('urlgen',views.makeurl,name="urlentry"),
    path('sharepoint/<lesson>/<st>',views.sharepoint,name="sharepoint"),
    path('admin/', admin.site.urls),
    
]
