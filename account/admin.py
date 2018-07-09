from django.contrib import admin
from .models import *
class ProfileAdmin(admin.ModelAdmin):
    model=Profile
    list_display = ['user','date_of_birth','photos']

# Register your models here.
class TechSkillAdmin(admin.ModelAdmin):
    model = TechSkill
    list_display=['skill_name',]

class LanguagesAdmin(admin.ModelAdmin):
    model=Languages
    list_display=['name']
    prepopulated_fields = {'slug': ('name',)}

# class MentorAdmin(admin.ModelAdmin):
#     model= Mentor
#     list_display=['profile',]

admin.site.register(Profile,ProfileAdmin)
admin.site.register(TechSkill,TechSkillAdmin)
admin.site.register(Languages,LanguagesAdmin)
# admin.site.register(Mentor,MentorAdmin)
