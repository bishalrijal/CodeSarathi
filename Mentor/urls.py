from django.urls import include,path
from django.conf.urls import url
from . import views 
from django.contrib.auth import views as auth_views
app_name='Mentor'
SOCIAL_AUTH_URL_NAMESPACE='social'

urlpatterns=[
    #path('login',views.MentorLogin,name='login'),
    path('login',auth_views.LoginView.as_view(template_name='mentor/login.html'),name='login'),
    path('logout',auth_views.logout,name='logout'),
    path('',views.Home,name='home'),

]