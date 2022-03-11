from django.urls import path
from .views import *

app_name = 'v4'
urlpatterns = [
    # path('', index, name='index'),
    path('', BaseView.as_view()),
    path('index', IndexView.as_view(), name='index'),
    path('html', HtmlView.as_view(), name='html'),
    path('name/<str:name>', NameView.as_view(), name='name'),
]