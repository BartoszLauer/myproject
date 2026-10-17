from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Lab 01</h1><p>Działa!</p>")