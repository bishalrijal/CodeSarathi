from django import forms 
from QA.models import Question,Answer,BlogPost,Comment


class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=('title','description','related')
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    description=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',}))
    

class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields=('answertext',)

class PostForm(forms.ModelForm):
    class Meta:
        model =BlogPost
        fields =('title','body')
    



class CommentForm(forms.ModelForm):
    comments = forms.CharField(required=False,
                               widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = ( 'comments',)
