from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView

from apps.posts.models import Posts
from apps.posts.serializers import PostsSerializers

class PostsAPIView(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializers
    
class PostCreateAPIView(CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializers