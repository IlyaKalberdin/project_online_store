from json import load
from django.core.management import BaseCommand
from catalog_app.models import Category, Product
from os.path import join


class Command(BaseCommand):
    """Удаляет все данные из БД и записывает новые"""

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()

        data = self.get_catalog_app_data(join('catalog_app_data.json'))

        category_list = []
        product_list = []

        for d in data:
            if 'category' in d['model']:
                category_list.append(Category(id=d['pk'],
                                              name=d['fields']['name'],
                                              description=d['fields']['description']))
            elif 'product' in d['model']:
                product_list.append(Product(id=d['pk'],
                                            name=d['fields']['name'],
                                            description=d['fields']['description'],
                                            image=d['fields']['image'],
                                            category=category_list[d['fields']['category'] - 1],
                                            price=d['fields']['price'],
                                            creation_date=d['fields']['creation_date'],
                                            last_modified_date=d['fields']['last_modified_date']))

        Category.objects.bulk_create(category_list)
        Product.objects.bulk_create(product_list)

    @staticmethod
    def get_catalog_app_data(path):
        with open(path) as file:
            data = load(file)

        return data
