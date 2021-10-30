from django.contrib import admin
from .models import Post, Comment



class CommentManager(admin.ModelAdmin):
    list_display = ('user', 'post', 'body')



admin.site.register(Post)
admin.site.register(Comment, CommentManager)