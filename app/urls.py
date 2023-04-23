from django.urls import path

from .views import index, posts

urlpatterns = [
    path('index/', index),
    path('home/', posts),
]
