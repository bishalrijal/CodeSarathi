from . import views
from django.urls import path
app_name = 'chat'
urlpatterns=[
   
    path('getmessage',views.getmessage,name='getmessage'),
    path('<username>/',views.Home,name='home'),

    path('<username>/post/', views.Post, name='post'),
    path('<username>/messages/', views.Messages, name='messages'),
    ]
#include chat.urls to main url