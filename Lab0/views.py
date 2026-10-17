from django.shortcuts import render

# Lista labów na stronie głównej - każdy nowy lab dopisz tutaj
LABY = [
    {"nazwa": "Lab 01", "opis": "Moje hobby: IT i oglądanie filmów", "url": "/lab01/"},
]


def home(request):
    return render(request, "home.html", {"laby": LABY})
