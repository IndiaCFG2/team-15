from django.contrib import admin
from django.urls import path
from . import views
from .views import line_chart, line_chart_json

urlpatterns = [

    path('result/',views.result,name="urlresult"),
    path('urlgen',views.makeurl,name="urlentry"),
    path('sharepoint/<lesson>/<st>',views.sharepoint,name="sharepoint"),
    path('admin/', admin.site.urls),
     path('chart', line_chart, name='line_chart'),
  path('chartJSON', line_chart_json, name='line_chart_json'),
    
]
