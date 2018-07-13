from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from account.models import Languages
from django.template.defaultfilters import slugify
from Mentor.models import Mentor
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

from django.utils import timezone
from django.urls import reverse
#from taggit.managers import TaggableManager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class BlogPost(models.Model):
    def get_absolute_url(self):
        return reverse('account:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])

    # tags = TaggableManager()
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250,null=True)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish',null=True)
    author = models.ForeignKey(Mentor,
                               related_name='blog_posts',
                               null=True,on_delete=True)
    body = models.TextField(blank=True)
    publish = models.DateTimeField(default=timezone.now,null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments',on_delete=False)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('created',)
    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)




