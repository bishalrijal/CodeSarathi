from django.db import models
from django.conf import settings as set
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


##for programming languages
class Languages(models.Model):
    name=models.CharField(max_length=200,blank=True, null=True,unique=True)
    slug=models.SlugField(max_length=50,blank=False,)

    def __str__(self):
        return self.name

# for technical skill one has or one has interest on 
class TechSkill(models.Model):
    languages=models.ManyToManyField(Languages)
    skill_name = models.CharField(max_length=2000, blank=True, null=True,)

    def __str__(self):
        return self.skill_name
        


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=False,primary_key=True)
    following = models.ManyToManyField(User,blank=True,related_name='followed_by')
    date_of_birth = models.DateField(blank=True,null=True)
    photos=models.ImageField(upload_to='users/%Y/%m/%d',blank=True,)
    bio = models.CharField(max_length=200,blank=True, null=True)


    @property
    def __repr__(self):
        return 'profile of {}'.format(self.user.username)

<<<<<<< HEAD
# class Mentor(models.Model):
#     profile=models.OneToOneField(User,on_delete=models.SET_NULL, null=True)
#     photos=models.ImageField(upload_to='mentor/%Y/%m/%d',blank=True,)
#     bio = models.CharField(max_length=200,blank=True, null=True)
#     skill = models.ManyToManyField(TechSkill,related_name='account_skill')
#     languages=models.ManyToManyField(Languages,related_name='account_language')

    def __str__(self):
        return '{}'.format(self.profile.username)
# Create your models here.
class Post(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    #created_by = models.ForeignKey(Profile,on_delete=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post= models.TextField(max_length=250,null=True)

    class Meta:
        ordering =('-created',)

    @property
    def _str__(self):
        return 'Post of {}'.format(self.user.username)
        #return self.user.user

"""@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()
"""
=======
>>>>>>> master
#-----------------------------------------------------------------------------------------------------blog
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
    author = models.ForeignKey(User,
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
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('created',)
    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


