from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound

def home(request):
    return render(request, "index.html")
# Create your views here.
