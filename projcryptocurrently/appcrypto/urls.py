from django.urls import path 

from .views import homepageview, coinview, reachview

urlpatterns = [
    path('', homepageview, name='homepageview'),
    path('coin/<coin_name>', coinview, name='coinview'),
    path('reach', reachview, name='reachview'),
]