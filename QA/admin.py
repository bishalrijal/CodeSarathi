from django.contrib import admin
from .models import Question,Answer

# class AnswerAdmin(admin.ModelAdmin):
#     model=Answer
#     fields=['question','answertext',]

admin.site.register(Answer)
admin.site.register(Question)

# Register your models here.
