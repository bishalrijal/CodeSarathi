from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Mentor

class SignupForm(UserCreationForm):
    email= forms.EmailField(max_length=200,help_text='Required')

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password1']!=cd['password2']:
            raise forms.ValidationError('Password don\'t match' )
        return cd['password2']

class InfoForm(forms.ModelForm):
    class Meta:
        model=Mentor
        fields=('bio','languages','github')
        
