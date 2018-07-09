from django.db import models
from django.contrib.auth.models import User
from account.models import TechSkill,Languages

# Create your models here.
class Mentor(models.Model):
    rating_choices=(

        (1,1),
        (2,2),
        (3,3),
                    )
    STATUS_CHOICE=(
        ('available','Available'),
        ('unavailable','Unavailable')
    )
    profile=models.OneToOneField(User,on_delete=models.CASCADE , null=True)
    photos=models.ImageField(upload_to='mentor/%Y/%m/%d',blank=True,)
    bio = models.CharField(max_length=200,blank=True, null=True)
    skill = models.ManyToManyField(TechSkill,related_name='mentor_skill')
    languages=models.ManyToManyField(Languages,related_name='mentor_language')
    rating=models.IntegerField(choices=rating_choices,null=True,blank=True)
    status=models.CharField(max_length=15,choices=STATUS_CHOICE,default='unavailable')
    github=models.URLField(max_length=200,null=True)
    def __str__(self):
        return '{}'.format(self.profile.username)
