from django.urls import path
from . import views

# Routing aplikacji - podpięty w Lab0/urls.py pod adresem "lab01/"
app_name = "lab01"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("gallery/", views.gallery, name="gallery"),
]
