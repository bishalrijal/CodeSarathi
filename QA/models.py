from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from account.models import Languages
from django.template.defaultfilters import slugify
@python_2_unicode_compatible
class Question(models.Model):
    """ Models class for Question and their associate 
    fields """
    title=models.CharField(max_length=200,blank=False)
    description=models.TextField(null=True,blank=True)
    pub_date=models.DateTimeField('date publish',auto_now_add=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    closed=models.BooleanField(default=False)
    upvote=models.IntegerField(default=0,blank=True)
    downvote=models.IntegerField(default=0,blank=True)
    related=models.ManyToManyField(Languages,blank=True,related_name='related_to')
    slug=models.SlugField(max_length=200,unique=True,blank=True,)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Question,self).save(*args,**kwargs)

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

# class notification(models.Model):
#     """models  for notification to the mentor if they 
#     ve a related question"""
#     message=models.CharField(max_length=200,)
#     user=models.ManyToManyField(settings.AUTH_USER_MODEL)
#     time=models.DateTimeField(auto_now=True)
    




