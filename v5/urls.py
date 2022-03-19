from django.urls import path
from .views import *

app_name = 'v5'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('result', ResultView.as_view(), name='result'),
    path('basic_form', BasicFormView.as_view(), name='basic_form'),
    path('done', DoneView.as_view(), name='done'),
]