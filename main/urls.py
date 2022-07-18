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
    # shared
    # staff url
    path('staff', views.staff, name="staff"),
    path('uabook_form/', views.uabook_form, name="uabook_form"),
    # publisher url
    path('student',views.SBookListView.as_view(), name="student"),
    # dashboard url
    path('dashboard', views.dashboard, name="dashboard"),
]