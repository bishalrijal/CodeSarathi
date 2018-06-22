from django.http import HttpResponse
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
            profile1=Mentor(profile=new_user)
            profile1.save()
            new_user.groups.add(group)
            return render(request,'step2.html',{'user':new_user})
    else:
        user_form=SignupForm()
    return render(request,'signup.html',{'form':user_form})

def Step2(request):
    if request.method =='POST':
        user_form=InfoForm(request.POST)
        if user_form.is_valid:
            user_info = user_form.save(commit=False)
            user_info.save()
            return HttpResponse("now you can log in ")
        else:
            return HttpResponse("invalied data")
    else:
        user_form=InfoForm()
    return render(request,'step2.html',{'form':user_form})
