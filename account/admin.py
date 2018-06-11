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

class MentorAdmin(admin.ModelAdmin):
    model= Mentor
    list_display=['profile',]

admin.site.register(Profile,ProfileAdmin)
admin.site.register(TechSkill,TechSkillAdmin)
admin.site.register(Languages,LanguagesAdmin)
admin.site.register(Mentor,MentorAdmin)


#admin.site.register(Profile)
admin.site.register(Post)
#------------------------------------------------------------------------------------------------------------
from django.contrib import admin
from .models import BlogPost,Comment,Profile,TechSkill,Languages,Mentor
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish',
                    'status')

    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
#Register your models here.

admin.site.register(BlogPost,PostAdmin)
admin.site.register(Comment, CommentAdmin)
