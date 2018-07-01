from django import forms 
from QA.models import Question,Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=('title','description','related')

class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields=('answertext',)