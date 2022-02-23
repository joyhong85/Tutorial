from django.urls import path
from .views import *

app_name = 'v2'
urlpatterns = [
    path('', index, name='index'),
    path('name', name, name='name'),
    path('name/<str:keyword>', username, name='username'),
]