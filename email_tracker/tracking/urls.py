from django.urls import path
from .views import *

urlpatterns = [
    path('track/', track_click, name='track_click'),
    path('clicks/', clicks_list, name='clicks_list'),
]