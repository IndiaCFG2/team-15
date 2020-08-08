from django.contrib import admin

# Register your models here.
from .models import AdminUser,School
admin.site.register(AdminUser)
admin.site.register(School)