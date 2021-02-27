from .models import User, Post, Project, Comment, Version, Tag
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class VersionSerializer(ModelSerializer):
    class Meta:
        model = Version
        fields = "__all__"

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
