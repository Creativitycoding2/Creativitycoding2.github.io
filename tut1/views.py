# file created by me - devlog
import os

from django.http import HttpResponse
from django.shortcuts import render


# pipeline

def home(request):
    return render(request, 'index.html')


def pipe1(request):
    file_path = os.path.join(os.path.dirname(__file__), '1.txt')
    with open(file_path) as f:
        file = f.read()
        f.close()
    return HttpResponse(f"{file} </br> <a href=/>back</a>")


def pipe2(request):
    return HttpResponse(f"test1 </br> <a href=/>back</a>")


def ecommerce(request):
    return HttpResponse(f"coming soon </br> <a href=/>back</a>")


def pipe3(request):
    return HttpResponse(f"test2 </br> <a href=/>back</a>")
