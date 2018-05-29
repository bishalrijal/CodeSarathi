from django.contrib import admin
from .models import Profile
class ProfileAdmin(admin.ModelAdmin):
    model=Profile
    list_display = ['user','date_of_birth','photos']
admin.site.register(Profile,ProfileAdmin)

# Register your models here.