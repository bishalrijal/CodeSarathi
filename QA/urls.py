from django.urls import include,path
from . import views

app_name='QA'

urlpatterns=[
    path('',views.home,name='home'),
    path('create',views.CreateQuestion,name='create'),
    path('delete/<int:id>/<slug:slug>',views.delete,name='delete'),
    path('edit/<int:id>/<slug:slug>',views.editquestion,name='edit'),
    path('filter-<slug:slug>',views.filter,name='filter'),
    path('myquestion',views.myquestion,name='myquestion'),
    path('<int:id>/<slug:slug>',views.detail,name='detail')

]