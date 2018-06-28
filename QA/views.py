from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .form import QuestionForm
from django.contrib import messages
from django.urls import reverse
from .models import Question,Answer
from django.contrib.auth.decorators import login_required


def home(request):
    question=Question.objects.all()
    question_form=QuestionForm()
    return render(request,'QA/home.html',{'Questions':question,'form':question_form})


def CreateQuestion(request):
    if request.method=='POST':
        question_form=QuestionForm(request.POST)
        if question_form.is_valid:
            newquestion=question_form.save()
            newquestion.user=request.user
            newquestion.save()
            messages.success(request,'question create succesfully!!')
        else:
            messages.error(request,'Question can\'t create try again')
    else:
        question_form=QuestionForm()
    
    return HttpResponseRedirect(reverse('QA:home'),{'form':question_form})







        
