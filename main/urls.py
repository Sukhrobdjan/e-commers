from django.contrib import admin
from .views import IndexView
from django.urls import path


app_name = 'main' # main:index


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]