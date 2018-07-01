from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .form import SignupForm,InfoForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from .models import Mentor
from django.urls import reverse
from django.contrib.auth.models import Group
group=Group.objects.get(name='mentor')
@login_required
def Home(request):
    return render(request, 'mentor/home.html')

# for signup 
def SignUp(request):
    if request.method == 'POST':
        user_form=SignupForm(request.POST)
        if user_form.is_valid:
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            new_user.groups.add(group)
            profile=Mentor(profile=new_user)
            new_user.save()
            login(request,new_user,backend='django.contrib.auth.backends.ModelBackend')            
            profile.save()
            return HttpResponseRedirect(reverse('Mentor:step2'))
    else:
        user_form=SignupForm()
    return render(request,'signup.html',{'form':user_form},)

def Step2(request):
    if request.method =='POST':
        user_form=InfoForm(request.POST)
        if user_form.is_valid:
            user_info = user_form.save(commit=False)
            user_info.save()
            return HttpResponseRedirect(reverse('Mentor:home'))
        else:
            return HttpResponse("invalied data")
    else:
        user_form=InfoForm()
    return render(request,'step2.html',{'form':user_form})
