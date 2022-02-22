from django.urls import path
from .views import *

app_name = 'v1'
urlpatterns = [
    path('', index, name='index'),
    path('redirect', index_redirect, name='index_redirect'),
    path('json', index_json, name='index_json'),
    path('file', index_file, name='index_file'),
]