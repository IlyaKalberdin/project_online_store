from django.db import models
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
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

    def send_letter(self, to_email: list):
        """Метод для отправки письма, если статья набрала 100 просмотров"""
        if self.count_views == 100:
            send_mail(
                'Больше 100 просмотров',
                f'Поздравляем! Ваша статья "{self.title}" набрала 100 просмотров',
                EMAIL_HOST_USER,
                recipient_list=to_email,
                fail_silently=False
            )

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блог'
