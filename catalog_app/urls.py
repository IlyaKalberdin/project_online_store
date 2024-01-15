from django.urls import path
from catalog_app.views import home_page, contact_page, product_page, create_product_page
from catalog_app.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', home_page, name='home'),
    path('contacts', contact_page, name='contacts'),
    path('product/<int:product_id>', product_page, name='product'),
    path('create-product', create_product_page, name='create_product')
]
