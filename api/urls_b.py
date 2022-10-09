from django.urls import path
from .views_b import *

urlpatterns = [
    path('add_product/', ADD)
]