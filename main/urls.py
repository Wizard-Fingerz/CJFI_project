from django.urls import path
from django.urls import re_path as url
from django_filters.views import FilterView

from . import views



urlpatterns = [
    path('', views.home,name = 'cjfi-home'),
]