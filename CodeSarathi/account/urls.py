from django.urls import path ,include
from . import views
from django.contrib.auth import views as authView


urlpatterns=[
   # path('login',views.user_login,name='login'),
    path('',views.Home,name='index'),
    path('login',authView.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('dashboard',views.Dashboard,name='dashboard'),
    path('register',views.Register,name='resister'),
    path('logout',authView.LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
    path('edit',views.edit_profile,name='edit'),
    path('oauth/complete/github/',include('social_django.urls',namespace='social')),
    path('become_a_mentor',authView.LoginView.as_view(template_name='mentor/login.html'),name='mentor_registration'),
    
    
]