from django.contrib import admin
from .models import Question,Answer
admin.site.register(Answer)
admin.site.register(Question)


from django.contrib import admin
from .models import BlogPost,Comment
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
    list_display = ('user', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('user', 'body')
#Register your models here.

admin.site.register(BlogPost,PostAdmin)
admin.site.register(Comment, CommentAdmin)

# Register your models here.
