from django.db import models
from django.urls import reverse
from users_app.models import User


NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='product_image/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за штуку')
    creation_date = models.DateField(verbose_name='дата создания')
    last_modified_date = models.DateField(verbose_name='дата последнего изменения')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')

    def __str__(self):
        # Строковое отображение объекта
        return (f'{self.name} {self.category} {self.price} '
                f'{self.creation_date} {self.last_modified_date} {self.description}')

    def get_absolute_url(self):
        return reverse('catalog_app:product', kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    number = models.CharField(max_length=10, verbose_name='номер')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.number}'

    class Meta:
        verbose_name = 'контакты'
        verbose_name_plural = 'контакты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='версия')
    number = models.IntegerField(verbose_name='номер версии')
    name = models.CharField(max_length=150, verbose_name='названии версии')
    is_current_version = models.BooleanField(default=False, verbose_name='это текущая версия')

    def __str__(self):
        return f'№{self.number}({self.name})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
