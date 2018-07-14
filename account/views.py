from django.shortcuts import render, get_object_or_404,reverse
from django.http import HttpResponse,HttpResponseRedirect 
from django.contrib.auth import authenticate, login
from .form import LoginForm ,UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import *
from QA.models import Question
from django.contrib.auth.models import Group
from django.urls import reverse


techskill=TechSkill.objects.all()
group=Group.objects.get(name='mentee')
def loginredirect(request):
    if request.user is not None:
        logged_in_user=request.user
        if logged_in_user.groups.get().name=='mentor':
            return HttpResponseRedirect(reverse('QA:mentor_home'))
        elif logged_in_user.groups.get().name=='mentee':
            return HttpResponseRedirect(reverse('QA:home'))
        else:
            return HttpResponse("user is not valied !!")

def videocall(request):
    return render(request,'webrtc/index.html')

def firstpage(request):
    return render(request,'01landingpage.html',{})


def Dashboard(request):
    techskill=TechSkill.objects.all()
    logged_in_user = request.user
    pic=Profile.objects.get(user=logged_in_user)
    picture=pic.photos
    posts = BlogPost.objects.filter(author=logged_in_user)
    if request.method == 'POST':
        Post_form = PostForm(data=request.POST)
        if Post_form.is_valid():
            new_Post = Post_form.save(commit=False)
            new_Post = Post_form.save()
            new_Post.author=request.user
            new_Post.slug=new_Post.title
            new_Post.save()
            return HttpResponseRedirect(reverse('account:dashboard'))
    else:
        Post_form=PostForm()
    return render(request,'account/dashboard.html',
                                    {'posts':posts,
                                    'post_form':Post_form,
                                    'media_url':settings.MEDIA_URL,
                                    'skill':techskill})
    
def Register(request):
    if request.method == 'POST':
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():

            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_user.groups.add(group)
            new_user.save()
            login(request,new_user,backend='django.contrib.auth.backends.ModelBackend')
            new_profile=Profile(user=new_user)
            new_profile.save()
        
            # return render(request,
            #              'account/registration_done.html',
            #              {'new_user':new_user}
            #              )
            #return HttpResponseRedirect(reverse('QA:home'))
            return HttpResponseRedirect(reverse('QA:home'),)         
    else:
        user_form=UserRegistrationForm()
    return render(request,
                        'account/register.html',
                        {'user_form':user_form})

@login_required
def edit_profile(request):
    if request.method=='POST':
        user_form=UserEditForm(instance=request.user,data=request.POST)
        profile_form=ProfileEditForm(instance=request.user.Profile,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form=UserEditForm(instance=request.user)
        profile_form=ProfileEditForm(instance=request.user.profile)

    return render(request,
                    'account/edit.html',
                    {'user_form':user_form,
                    'profile_form':profile_form
                    })

from django.db.models import Q
from Mentor.models import Mentor
def MentorSearch(request,slug):
    query=slug
    if query:
        result=Mentor.objects.filter(Q(profile__username__icontains=query)|
        Q(skill__skill_name__icontains=query)|
        Q(languages__name__icontains=query)
        ).distinct()
        return render(request,'search/index.html',{'result':result })


    else:
        msg="No result found for search"

        return render(request,'search/index.html',{'message':msg })



