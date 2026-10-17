from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lab01/', include('lab01.urls')),
    path('admin/', admin.site.urls),
]
