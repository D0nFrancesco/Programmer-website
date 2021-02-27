import rest_framework
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.views.generic import TemplateView
from .serializers import PostSerializer
from .models import Post


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostLisDetailView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
