from . import views
from django.urls import path
app_name = 'chat'
urlpatterns=[
   # path('',views.Login,name='login'),
    #path('<user:username2>/',views.login,name='login'),
    #path('login/',views.Login,name='login'),
    #path('logout/', views.Logout, name='logout'),
    #path('home/', views.Home, name='home'),
    path('<username>/',views.Home,name='home'),

    path('<username>/post/', views.Post, name='post'),
    path('nirajan/messages/', views.Messages, name='messages'),
    ]
#include chat.urls to main url