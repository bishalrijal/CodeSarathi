from django.urls import path ,include
from . import views
from django.contrib.auth import views as authView

app_name = 'account'


urlpatterns=[
   # path('login',views.user_login,name='login'),
    path('',views.firstpage,name='firstpage'),
    path('login',authView.LoginView.as_view(template_name='registration/login.html',),name='login'),
    path('loginredirect',views.loginredirect,name='loginr'),
    path('dashboard',views.Dashboard,name='dashboard'),
    path('register',views.Register,name='register'),
    path('logout',authView.logout_then_login,name='logout'),
    path('edit',views.edit_profile,name='edit'),
    path('become_a_mentor',authView.LoginView.as_view(template_name='mentor/login.html'),name='mentor_registration'),
    path('<slug:slug>-mentor',views.MentorSearch,name='searchmentor'),

    path('videocall',views.videocall,name='videocall')
    

]