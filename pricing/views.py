from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def about(request):
    return HttpResponse("<p>Hello, Its me, can you hear me?</p>")