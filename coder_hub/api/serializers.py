from .models import User, Post, Project, Comment, Votes, Version, Tag
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    classMeta:
    model = Article
    fields = ('title', 'content')