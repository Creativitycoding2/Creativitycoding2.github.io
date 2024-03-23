from django.shortcuts import render, HttpResponse

# Create your views here.


def ecommerce(request):
    return render(request, 'ecommerce.html')


def signin(request):
    return HttpResponse("hello world")


def cart(request):
    return HttpResponse("hello world")


def search(request):
    return render(request, "query.html")


def product(request):
    return HttpResponse("coming soon")
