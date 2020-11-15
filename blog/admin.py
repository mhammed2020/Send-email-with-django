from django.contrib import admin
from .models import Post,Comment,Book
from blog.models import Project

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Project)
admin.site.register(Book)