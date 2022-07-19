from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    # general urls
    path('', views.home, name="index"),
    path('home', views.login_form, name="home"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logoutView, name="logout"),
    path('regform/', views.register_form, name="regform"),
    path('register/', views.registerView, name="register"),
    path('about/', views.about, name="about"),
    
    # shared
   
    # staff url
    path('staff', views.staff, name="staff"),
    path('uabook_form/', views.uabook_form, name="uabook_form"),
    path('uabook/', views.uabook, name="uabook"),
    
    # student url
    path('student',views.UBookListView.as_view(), name="student"),
    path('feedback_form/', views.feedback_form, name="feedback_form"),
    path('send_feedback/', views.send_feedback, name="send_feedback"),
    path('ucchat/', views.UCreateChat.as_view(), name="ucchat"),
    path('ulchat/', views.UListChat.as_view(), name="ulchat"),
    
    # dashboard url
    path('dashboard', views.dashboard, name="dashboard"),
]