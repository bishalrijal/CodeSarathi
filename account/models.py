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
