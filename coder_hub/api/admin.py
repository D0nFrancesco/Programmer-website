from django.contrib import admin
from .models import User, Post, Tag, Comment, Project, Version

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Project)
admin.site.register(Version)

from .models import Post

admin.site.register(Post)
