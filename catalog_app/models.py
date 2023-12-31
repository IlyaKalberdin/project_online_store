from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='product_image/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за штуку')
    creation_date = models.DateField(verbose_name='дата создания')
    last_modified_date = models.DateField(verbose_name='дата последнего изменения')

    def __str__(self):
        # Строковое отображение объекта
        return (f'{self.name} {self.category} {self.price} '
                f'{self.creation_date} {self.last_modified_date} {self.description}')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.description}'

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
