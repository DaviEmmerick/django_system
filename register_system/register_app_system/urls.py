# register_app_system/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('register_system.urls')), # Inclui as URLs do seu aplicativo
]