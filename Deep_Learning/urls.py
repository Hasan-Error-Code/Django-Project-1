from django.contrib import admin
from django.urls import path, include
from Home import urls
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('deep/', views.deep),
]
