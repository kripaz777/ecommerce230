from django.contrib import admin
from django.urls import path
from .views import *

app_name = "home"
urlpatterns = [
    path('',HomeView.as_view(),name = 'home'),
    path('product/<slug>',ProductDetailView.as_view(),name = 'product'),
]