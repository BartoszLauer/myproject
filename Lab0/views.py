from django.shortcuts import render

# Lista labów na stronie głównej - każdy nowy lab dopisz tutaj
LABY = [
    {"nazwa": "Lab 1", "opis": "Moje hobby", "url": "/lab01/"},
]


def home(request):
    return render(request, "home.html", {"laby": LABY})
