from django.db import models
from datetime import datetime

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    text = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='blog_image/', verbose_name='изображение', **NULLABLE)
    creation_date = models.DateField(default=datetime.now(), verbose_name='дата создания')
    is_published = models.BooleanField(default=False, verbose_name='опубликовано ли')
    count_views = models.IntegerField(default=0, verbose_name='кол-во просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блог'
