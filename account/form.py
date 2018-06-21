from django import forms
from .models import Comment
from django.contrib.auth.models import User
from .models import Profile,Post
class LoginForm(forms.Form):
    class Meta:
        model=User
        fields=('username','password')
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholer':'Username','id':'id="exampleDropdownFormEmail1"'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','id':'exampleDropdownFormPassword1'}))
class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields =('post',)

class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(label='Password',
                            widget=forms.PasswordInput(attrs={'class':'form-control','name':'password','id':'password'}))
    password2=forms.CharField(label='Repeat password',
                              widget=forms.PasswordInput(attrs={'class':'form-control','name':'password2','id':'password2'}))
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'class': 'form-control', 'name':'username','id':'username'}))
    first_name = forms.CharField(label='firstname', widget=forms.TextInput(
        attrs={'class': 'form-control', 'name': 'firstname', 'id': 'firstname'}))
    last_name = forms.CharField(label='lastname', widget=forms.TextInput(
        attrs={'class': 'form-control', 'name': 'lastname', 'id': 'lastname'}))
    email = forms.EmailField(label='email', widget=forms.TextInput(
        attrs={'class': 'form-control', 'name': 'email', 'id': 'email'}))
    class Meta:
        model= User
        fields={'username','first_name','last_name','email'}
    
    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('Password don\'t match' )
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('first_name','last_name','email',)

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=('date_of_birth','photos')
class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=25,widget=forms.TextInput(attrs={'class':'form-group','placeholder':'enter name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-group','placeholder':'enter email'}))
    comments = forms.CharField(required=False,
                               widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = ('name', 'email', 'comments')