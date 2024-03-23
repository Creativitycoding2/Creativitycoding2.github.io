from django.urls import path
from . import views

urlpatterns = [
    path('/', views.ecommerce, name='index3'),
    path('/sign', views.signin, name='index03'),
    path('/cart', views.cart, name='index13'),
    path('/search', views.search, name='index23'),
    path('/product', views.product, name='index33')
]