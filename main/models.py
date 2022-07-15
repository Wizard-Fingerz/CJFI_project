from django.db import models
import django_filters

# Create your models here.
LEVEL_CHOICES = [
        ("UNDERGRADUATE", "UNDERGRADUATE"),
        ("POSTGRADUATE", "POSTGRADUATE"),
        ("DEGREE APPRENTICESHIP", "DEGREE APPRENTICESHIP"),
        ("LEARNING AT WORK", "LEARNING AT WORK"),
        ("DISTANT LEARNING", "DISTANT LEARNING"),
        ("SHORT COURSES AND CPD", "SHORT COURSE AND CPD"),
    ]

class Course(models.Model):
    level = models.CharField(max_length=30, choices = LEVEL_CHOICES, default= 'UNDERGRADUATE')
    title = models.CharField(max_length= 250)
    keyword = models.CharField(max_length = 200)


class CourseFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    level = django_filters.ChoiceFilter(choices=LEVEL_CHOICES)
    class Meta:
        model = Course
        fields = ['level', 'title', 'keyword',]