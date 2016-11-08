from django.contrib import admin
from myHealthGroup.Apps.Blog.models import Post, Like

admin.site.register(Post)
admin.site.register(Like)