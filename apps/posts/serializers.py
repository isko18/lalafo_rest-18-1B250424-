from rest_framework import serializers
from apps.posts.models import Posts

class PostsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'