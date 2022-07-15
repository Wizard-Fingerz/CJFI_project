from django import forms
from .models import Course
from django.contrib.auth.forms import UserCreationForm


class CourseSearch(UserCreationForm):
    title = forms.CharField()

    class Meta:
        model = Course
        fields = ['level', 'title']