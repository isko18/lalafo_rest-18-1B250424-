from django.urls import path

from apps.posts.views import PostsAPIView, PostCreateAPIView

urlpatterns = [
    path('', PostsAPIView.as_view(), name='api_posts'),
    path('create', PostCreateAPIView.as_view(), name='api_posts_create')
]
