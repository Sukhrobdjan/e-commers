from django.contrib import admin
from .views import IndexView, CategoyrView
from django.urls import path


app_name = 'main'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<str:category_name>/category ', CategoyrView.as_view(), name='category'),
]