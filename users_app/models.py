from django.contrib.auth.models import AbstractUser
from django.db import models
from catalog_app.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='почта', unique=True)
    is_confirmed_email = models.BooleanField(default=False, verbose_name='почта подтверждена')

    avatar = models.ImageField(verbose_name='аватар', **NULLABLE)
    number = models.CharField(max_length=50, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

