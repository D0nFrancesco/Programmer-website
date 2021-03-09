from .models import User, Post, Project, Comment, Version, Tag
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.views.generic import ListView

class PostSerializer(serializers.ModelSerializer):

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
    

class PostListView(ListView):
    model = Post



#Comment Serializer
@api_view(['GET', ])
def api_detail_comment_view(request, slug):

    try:
        comment_post = CommentPost.objects.get(slug=slug)
    except Comment.Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CommentPostSerializer(comment_post)
        return Response(serializer.Data)

#Comment Serializer
@api_view(['PUT', ])
def api_update_comment_view(request, slug):

    try:
        comment_post = CommentPost.objects.get(slug=slug)
    except Comment.Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #if not working or unnessesari remove it
    if request.method == 'PUT':
        serializer = CommentPostSerializer(comment_post, data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save
            data["sucess"] = "update successful"
            return Response(data=data)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Comment Serializer
@api_view(['DELETE', ])
def api_delete_comment_view(request, slug):

    try:
        comment_post = CommentPost.objects.get(slug=slug)
    except Comment.Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        operation = comment_post.delete()
        data = {}
        if operation:
            data.["success"] = "delete succesfull"
            else:               #Text can be changed
                data["failure"] = "delete failed"
                return Response(data=data)
                
#Comment Serializer
@api_view(['POST', ])
def api_create_comment_view(request):

account = Account.objects.get(pk=1)
comment_post = CommentPost(author=account)

if request.methode == 'POST':
    serializer = CommentPostSerializer(blog_post, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Tag Serializer
@api_view(['GET', ])
def api_detail_tag_view(request, slug):

    try:
        tag_name = TagName.objects.get(slug=slug)
    except Tag.Name.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TagNameSerializer(tag_name)
        return Response(serializer.Data)