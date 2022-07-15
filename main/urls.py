from django.urls import path
from django.urls import re_path as url
from django_filters.views import FilterView
from .models import CourseFilter
from . import views



urlpatterns = [
    path('', views.home,name = 'cjfi-home'),
    url(r'^search/$', FilterView.as_view(filterset_class=CourseFilter,
        template_name='search_results.html'), name='search'),
]