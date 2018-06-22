from django.contrib import admin
from .models import Mentor

class MentorAdmin(admin.ModelAdmin):
    model=Mentor
    list_display=['profile','status']

admin.site.register(Mentor,MentorAdmin)
# Register your models here.
