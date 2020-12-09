from django.urls import path
from .views import home

app_name = 'news'

urlspatterns = [
    path('', home, name = 'homepage_news'),
]