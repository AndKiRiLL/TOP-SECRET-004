from App.views import *
from django.urls import path

urlpatterns = [
    path('', index, name='news_all'),
    path('news_political/', news_political, name='news_political'),
    path('news_economic/', news_economic, name='news_economic'),
    path('news_sport/', news_sport, name='news_sport'),
    path('news_cooking/', news_cooking, name='news_cooking'),
    path('news_nature/', news_nature, name='news_nature'),
    path('news_construction/', news_construction, name='news_construction'),
    path('create/', create, name='create'),
    path('delete/<int:id>/', delete, name='delete'),
    path('edit/<int:id>/', edit, name="edit"),
]