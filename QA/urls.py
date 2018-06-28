from django.urls import include,path
from . import views

app_name='QA'

urlpatterns=[
    path('',views.home,name='home'),
    path('create',views.CreateQuestion,name='create'),
]