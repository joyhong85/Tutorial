from django.urls import path
from .views import *

app_name = 'v4'
urlpatterns = [
    # path('', index, name='index'),
    path('', BaseView.as_view()),
    # path('', IndexView.as_view(), name='index'),
    # path('name', name, name='name'),
    path('name/<str:keyword>', NameView.as_view()),
    # path('name/<str:keyword>', username, name='username'),
]