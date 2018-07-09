from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Mentor

class SignupForm(UserCreationForm):
    email= forms.EmailField(max_length=200,help_text='Required')

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholer':'Username',}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholer':'Firstname',}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholer':'lastname',}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholer':'email',}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholer':'password',}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholer':'RepeatPassword',}))

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password1']!=cd['password2']:
            raise forms.ValidationError('Password doesn\'t match' )
        return cd['password2']
 
class InfoForm(forms.ModelForm):
    class Meta:
        model=Mentor
        fields=('bio','languages','github')
        
    bio=forms.CharField(widget=forms.Textarea(attrs={'rows':4,'cols':40, 'class':'form-control','placeholer':'bio',}))
    github=forms.URLField(initial='https://github.com/')

