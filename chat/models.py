from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender',default="")
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver',default="")
    message = models.TextField()

    def __str__(self):
        return self.message