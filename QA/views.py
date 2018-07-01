from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from .form import QuestionForm
from django.contrib import messages
from django.urls import reverse
from .models import Question,Answer
from account.models import Languages
from django.contrib.auth.decorators import login_required


def home(request):
    question=Question.objects.all()
    question_form=QuestionForm()
    language=Languages.objects.all()
    return render(request,'QA/home.html',{'Questions':question,'form':question_form,'languages':language})


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
    
    return HttpResponseRedirect(reverse('QA:home'),)

def delete(request,id,slug):
    question=get_object_or_404(Question,id=id,slug=slug)
    question.delete()
    return HttpResponseRedirect(reverse('QA:home'))


def filter(request,slug):
    lang=slug
    if lang:
        result=Question.objects.filter(related__name=lang)
        return render(request,'QA/filter.html',{'Questions':result})
    else:
        return HttpResponse('this is not valid Querry')

@login_required
def myquestion(request):
    if request.user.is_authenticated:
        result=Question.objects.filter(user=request.user)
        return render(request,'QA/myquestion.html',{'Questions':result})
    else:
        return HttpResponse('this is not valid Querry')



def editquestion(request,id,slug):
    question=get_object_or_404(Question,id=id,slug=slug)
    if request.method=='POST':
        editform=QuestionForm(instance=question,data=request.POST)
        if editform.is_valid:

            editform.save()
            return HttpResponseRedirect(reverse('QA:home'))
    else:
        editform=QuestionForm(instance=question)

    return render(request,'QA/edit.html',{'form':editform,'Question':question})

from .form import AnswerForm
def detail(request,slug,id):
    question=get_object_or_404(Question,slug=slug,id=id)
    Answers=Answer.objects.filter(question=question)
    if request.method == 'POST':
        answerform=AnswerForm(data=request.POST)
        if answerform.is_valid():
            newanswer=answerform.save(commit=False)
            newanswer.user=request.user
            newanswer.question=question
            newanswer.save()
            return HttpResponseRedirect(reverse('QA:detail',kwargs={'slug':question.slug,'id':question.id}))
    else:
        answerform=AnswerForm()
        return render(request,'QA/answer.html',{'question':question,'Answers':Answers,'answerform':answerform})
    
