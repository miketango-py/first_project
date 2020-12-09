from django.urls import path
from .views import home

app_name = 'news_app'

urlspatterns = [
    path('homepage_news/', home, name = 'homepage_news'),
]