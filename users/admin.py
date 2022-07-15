from django.contrib import admin
from .models import Profile, Staff, Student
# Register your models here.


admin.site.register([Profile, Staff, Student])