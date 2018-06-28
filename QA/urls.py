from django.urls import include,path
from . import views

app_name='QA'

urlpatterns=[
    path('',views.home,name='home'),
    path('create',views.CreateQuestion,name='create'),
    path('delete/<int:id>/<slug:slug>',views.delete,name='delete'),
    path('edit/<int:id>/<slug:slug>',views.editquestion,name='edit')
]