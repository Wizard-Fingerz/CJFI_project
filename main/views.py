from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.mixins import PassRequestMixin
from .models import User, Book
from django.contrib import messages
from django.db.models import Sum
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from . import models
import operator
import itertools
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, logout
from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.



def home(request):
    return render(request, 'main/index.html')

def login_form(request):
    return render(request, 'main/login.html')


def logoutView(request):
    logout(request)
    return redirect('home')


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            if user.is_admin or user.is_superuser:
                return redirect('dashboard')
            elif user.is_staff:
                return redirect('staff')
            else:
                return redirect('student')
        else:
            messages.info(request, "Invalid Username or password")
            return redirect('home')


def register_form(request):
    return render(request, 'student/register.html')

def registerView(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password = make_password(password)

        a = User(username = username, email = email, password=password)
        a.save()
        messages.success(request, "Account was created successfully")
        return redirect('home')
    else:
        messages.error(request, 'Registration Fail, try again later')
        return redirect('regform')


# staff views
def staff(request):
    return render(request, 'staff/home.html')


# student views
def student(request):
    return render(request, 'student/home.html')

def uabook_form(request):
    return render(request, 'student/add_book.html')

class SBookListView(ListView):
    model = Book
    template_name = 'student/book_list.html'
    context_object_name = 'books'
    Paginate_by = 4
    
    def get_queryset(self):
        return Book.objects.order_by('-id')

# Admin views
def dashboard(request):
    return render(request, 'dashboard/home.html')
