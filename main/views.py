from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.mixins import PassRequestMixin
from .models import User, Book, Chat, Feedback
from django.contrib import messages
from django.db.models import Sum
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from .forms import ChatForm
from . import models
import operator
import itertools
import datetime
from django.utils import timezone
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

@login_required
def feedback_form(request):
    return render(request, 'student/send_feedback.html')

@login_required
def send_feedback(request):
        if request.method == 'POST':
                feedback = request.POST['feedback']
                current_user = request.user
                user_id = request.user
                user_id = current_user.id
                username = current_user.username
                feddback = username + "says" + feedback

                a = Feedback(feedback=feedback)
                a.save()
                messages.success(request, 'Request was sent')
                return redirect('feedback_form')
        else:
            messages.error(request, 'feedback was not sent')
            return redirect('feedback_form')

def about(request):
    return render(request, 'about.html')
# staff views
def staff(request):
    return render(request, 'staff/home.html')
def uabook_form(request):
    return render(request, 'staff/add_book.html')


# student views

def student(request):
    return render(request, 'student/home.html')



class UBookListView(ListView):
    model = Book
    template_name = 'student/book_list.html'
    context_object_name = 'books'
    Paginate_by = 4
    
    def get_queryset(self):
        return Book.objects.order_by('-id')

def uabook(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        year = request.POST['year']
        publisher = request.POST['publisher']
        desc = request.POST['desc']
        cover = request.FILES['cover']
        pdf = request.FILES['pdf']
        current_user = request.user
        user_id = current_user.id
        username = current_user.username
        
        a = Book(title=title, author=author,year=year,publisher=publisher,desc=desc,cover=cover, pdf=pdf, uploaded_by = username, user_id=user_id)
        a.save()
        messages.success(request, 'Book was uploaded Successfully')
        return redirect('student')
    else:
        messages.error(request, 'Book was not uploaded succesfully')
        return redirect('uabook_form')

class UCreateChat(LoginRequiredMixin, CreateView):
    form_class = ChatForm
    model = Chat
    template_name = 'student/chat_form.html'
    success_url = reverse_lazy('student')
    
    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.user = self.request.user
        self.object.save()
        return Super().form_valid(form)

class UCreateChat(LoginRequiredMixin, CreateView):
    form_class = ChatForm
    model = Chat
    template_name = 'student/chat_form.html'
    success_url = reverse_lazy('ulchat')

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class UListChat(LoginRequiredMixin, ListView):
    model = Chat
    template_name = 'student/chat_list.html'

    def get_queryset(self):
        return Chat.objects.filter(posted_at__lte=timezone.now()).order_by('-posted_at')


# Admin views
def dashboard(request):
    return render(request, 'dashboard/home.html')
