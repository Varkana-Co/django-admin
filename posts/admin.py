from django.contrib import admin

from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display=['id','title', 'is_enable', 'publish_date', 'created_time', 'updated_time']


class CommentAdmin(admin.ModelAdmin):
    list_display=['post', 'text_comment', 'created_time']



admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
