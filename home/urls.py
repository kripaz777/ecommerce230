from django.contrib import admin
from django.urls import path
from .views import *

app_name = "home"
urlpatterns = [
    path('',HomeView.as_view(),name = 'home'),
    path('product/<slug>',ProductDetailView.as_view(),name = 'product'),
    path('search', SearchView.as_view(), name='search'),
    path('category/<slug>', CategoryView.as_view(), name='category'),
    path('signup',register,name = 'signup'),
    path('signin',signin,name = 'signin'),
    path('mycart',ViewCart.as_view(),name = 'mycart'),
    path('add-to-cart/<slug>',cart,name = 'add-to-cart'),
    path('delete-cart/<slug>',deletecart,name = 'delete-cart'),
    path('delete-single-cart/<slug>',delete_single_cart,name = 'delete-single-cart'),
]