from django.urls import path

from apps.posts.views import PostsAPIView, PostCreateAPIView, PostUpdateAPIVew, PostDestroyAPIView

urlpatterns = [
    path('', PostsAPIView.as_view(), name='api_posts'),
    path('create', PostCreateAPIView.as_view(), name='api_posts_create'),
    path('update/<int:pk>/', PostUpdateAPIVew.as_view(), name='api_posts_update'),
    path('delete/<int:pk>/', PostDestroyAPIView.as_view(), name='api_posts_delete')
]