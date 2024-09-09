from django.urls import path

from apps.categories.views import CategoryCreateAPIView, CategoryDestoyAPIVeiw, CategoryRetrieveAPIView, CategoryUpdateAPIView, CategoryAPIView

urlpatterns = [
    path('', CategoryAPIView.as_view(), name='api_category'),
    path('<int:pk>/', CategoryRetrieveAPIView.as_view(), name='api_category_retrieve/'),
    path('create/', CategoryCreateAPIView.as_view(), name='api_category_create/'),
    path('update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='api_category_update/'),
    path('delete/<int:pk>/', CategoryDestoyAPIVeiw.as_view(), name='api_category_delete/')
]