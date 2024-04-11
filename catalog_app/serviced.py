from django.core.cache import cache
from catalog_app.models import Category
from config.settings import CACHE_ENABLED


def category_cache_example():
    if CACHE_ENABLED:
        key = 'category'
        category = cache.get(key)

        if category is None:
            category = Category.objects.all()
            cache.set(key, category)
    else:
        category = Category.objects.all()

    return category
