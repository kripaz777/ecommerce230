from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('item', ItemViewSet)
router.register('cart', CartViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('filter-item', ItemFilterListView.as_view(),name = 'filter-item'),
]