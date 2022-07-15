from django.shortcuts import render
from .models import Course
from .filters import CourseFilter
# Create your views here.

def home(request):
    return render(request, 'index.html')



def search(request):
    course_list = Course.objects.all()
    course_filter = CourseFilter(request.GET, queryset=course_list)
    return render(request, 'search_results.html', {'filter': course_filter})