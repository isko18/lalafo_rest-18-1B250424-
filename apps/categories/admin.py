from django.contrib import admin
from apps.categories.models import Category
# Register your models here.

@admin.register(Category)
class CategoryADmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created')
    prepopulated_fields = {'slug': ('title', )}