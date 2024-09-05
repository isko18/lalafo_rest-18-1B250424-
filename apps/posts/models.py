from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название товара'
    )
    description = models.TextField(
        verbose_name='Описание товара'
    )
    image = models.ImageField(
        upload_to='post_image/',
        verbose_name='фото товара'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создание'
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'