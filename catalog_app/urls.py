from django.urls import path
from catalog_app.views import home_page, contact_page, product_page

urlpatterns = [
    path('', home_page),
    path('contacts', contact_page),
    path('product/<int:product_id>', product_page)
]
