from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    slug = models.SlugField(
        verbose_name="Человека понятный URL"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"