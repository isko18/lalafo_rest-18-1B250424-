from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from apps.posts.models import Posts
from apps.posts.serializers import PostsSerializers

class PostsAPIView(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializers
    
class PostCreateAPIView(CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializers
    
class PostUpdateAPIVew(UpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializers
    
class PostDestroyAPIView(DestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializers 
