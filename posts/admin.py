from django.contrib import admin
from django.urls import reverse
from django.utils import html
from .models import Post, Comment, Vote



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'slug',
        'created',
        )
    readonly_fields = ('show_url',)

    def show_url(self, instance):
        url = reverse(
            'posts:post_detail',
            kwargs={
                'year': instance.created.year,
                'month': instance.created.month,
                'day': instance.created.day,
                'slug': instance.slug,
            }
        )
        response = html.format_html("""<a href="{0}"> {0} </a>""", url)
        return response



@admin.register(Comment)
class CommentManager(admin.ModelAdmin):
    list_display = (
        'user',
        'post',
        'body',
        )



admin.site.register(Vote)
