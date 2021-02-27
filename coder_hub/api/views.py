from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import PostSerializer, UserSerializer
from .models import Post, User


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostLisDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
