from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializerV2


# Create your views here.
def index(request):
    ...


def for_id(request):
    ...


class PostListV3(generics.ListCreateAPIView):
    queryset = Post.objects.all() # 
    serializer_class = PostSerializerV2


class PostDetailV3(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializerV2


