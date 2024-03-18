from django.urls import path
from . import views

urlpatterns = [
    path('/', views.textutils, name='index3'),
    path('/perform', views.result_text, name='index5')
]
