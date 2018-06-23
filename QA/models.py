from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
@python_2_unicode_compatible
class Question(models.Model):
    """ Models class for Question and their associate 
    fields """
    slug=models.SlugField(max_length=200)
    title=models.CharField(max_length=200,blank=False)
    description=models.TextField()
    pub_date=models.DateTimeField('date publish',auto_now_add=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,primary_key=True,on_delete=models.CASCADE)
    closed=models.BooleanField(default=False)
    upvote=models.IntegerField(default=0)
    downvote=models.IntegerField(default=0)

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Answer(models.Model):
    """ Models class for Question and their associate 
    fields """
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    answertext=models.TextField()
    pub_date=models.DateTimeField('date published ',auto_now_add= True)
    updated=models.DateTimeField('date updated',auto_now=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    answer=models.BooleanField(default=True)
    upvote=models.IntegerField(default=0)
    downvote=models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    def __str__(self):
        return self.answertext


