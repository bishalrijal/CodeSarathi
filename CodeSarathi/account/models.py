from django.db import models
from django.conf import settings as set
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

##for programming languages
class Languages(models.Model):
    name=models.CharField(max_length=200,blank=True, null=True,unique=True)

    def __str__(self):
        return self.name

# for technical skill one has or one has interest on 
class TechSkill(models.Model):
    languages=models.ManyToManyField(Languages,null=True)
    skill_name = models.CharField(max_length=2000, blank=True, null=True,)

    def __str__(self):
        return self.skill_name
        

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=False)
    date_of_birth=models.DateField(blank=True,null=True)
    photos=models.ImageField(upload_to='users/%Y/%m/%d',blank=True,)
    bio = models.CharField(max_length=200,blank=True, null=True)
    skill = models.ForeignKey(TechSkill, on_delete=models.CASCADE,null=True,related_name='sklii')
    languages=models.ForeignKey(Languages,on_delete=models.CASCADE,to_field='name',null=True)
    def __str__(self) :
        return 'profile of {}'.format(self.user.user_name)

# Create your models here.
"""@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()
"""

"""class Mentor(models.Model):
    profile=models.OneToOneField(Profile,on_delete=models.SET_NULL)"""