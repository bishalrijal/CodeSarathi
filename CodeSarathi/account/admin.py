from django.contrib import admin
from .models import Profile,TechSkill,Languages
class ProfileAdmin(admin.ModelAdmin):
    model=Profile
    list_display = ['user','date_of_birth','photos']

class TechSkillAdmin(admin.ModelAdmin):
    model = TechSkill
    list_display=['skill_name',]

class LanguagesAdmin(admin.ModelAdmin):
    model=Languages
    list_display=['name']

admin.site.register(Profile,ProfileAdmin)
admin.site.register(TechSkill,TechSkillAdmin)
admin.site.register(Languages,LanguagesAdmin)