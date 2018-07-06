from django import forms 
from QA.models import Question,Answer


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