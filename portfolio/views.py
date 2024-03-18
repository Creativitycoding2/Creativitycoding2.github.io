from django.shortcuts import render

# Create your views here.


def portfolio(request):
    params = {"name": "Tanush", "profession": "Web Developer"}
    return render(request, 'rendertemp.html', params)