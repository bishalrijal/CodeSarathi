from django import forms 
from QA.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=('title','description','related')
