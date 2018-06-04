from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth import authenticate, login
from .form import LoginForm ,UserRegistrationForm,UserEditForm,ProfileEditForm
from .models import *

"""def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authentication successfully')

                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalied Login')
        
    else:
        form = LoginForm()
            
    return render(request, 'account/login.html', {'form' : form })
    """
from django.contrib.auth.decorators import login_required 
from django.views.generic import ListView
"""class TechSkillList(ListView):
    model= TechSkill
    context_object_name='skills'
    def  get_context_data(self,**kwargs):
        context = super(TechSkillList,self).get_context_data(**kwargs)
        context['languages']=TechSkill
        return context"""

def Home(request):
    s_list=[]
    Lang=[]
    s_no=TechSkill.objects.all().count()
    for i in range(s_no):
        t=TechSkill.objects.all()[i]
        s_list.append(t.skill_name)
        l_no=t.languages.all().count()
        l=[]
        for j in range(l_no):
            l.append(t.languages.all()[j].name)
        Lang.append(l)

    return render(request,'base.html',{'skills':s_list,'languages':Lang})
    
    
        

@login_required
def Dashboard(request):
    return render(request,'account/dashboard.html')
    
def Register(request):
    if request.method == 'POST':
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            profile=Profile.objects.create(user=new_user)
            new_user.save()
            
            return render(request,
                         'account/registration_done.html',
                         {'new_user':new_user}
                         )
                        
    else:
        user_form=UserRegistrationForm()
    return render(request,
                        'account/register.html',
                        {'user_form':user_form})

# Create your views here.
##profile edit view here
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
                    