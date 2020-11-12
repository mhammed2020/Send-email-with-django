from django.contrib import admin
from .models import Post,Comment
from blog.models import Project

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Project)