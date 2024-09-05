from django.contrib import admin
from apps.posts.models import Posts
# Register your models here.

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created')
    search_fields = ('title', 'description')