from django.contrib import admin
from django.urls import path, include
from Home import urls
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('machine/', views.machine, name="machine"),
    path('dt/', views.dt, name="dt"),
    path('knn/', views.knn, name="knn")
]
