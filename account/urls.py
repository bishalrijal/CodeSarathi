from django.urls import path 
from . import views
from django.contrib.auth import views as authView

app_name = 'account'


urlpatterns=[
   # path('login',views.user_login,name='login'),
    path('',views.firstpage,name='firstpage'),
    path('blog',views.post_list,name='blog'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>',views.post_detail,name='post_detail'),
    path('login',authView.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('dashboard',views.Dashboard,name='dashboard'),
    path('register',views.Register,name='register'),
    path('logout',authView.LogoutView.as_view(template_name='registration/logout.html'),name='logout'),


]