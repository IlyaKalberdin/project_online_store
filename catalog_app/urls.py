from django.urls import path
from catalog_app.views import (ProductListView, contact_page, ProductDetailView,
                               ProductCreateView, ProductUpdateView, ProductDeleteView,
                               UserProductListView, ModeratorProductUpdateView)

from catalog_app.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts', contact_page, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create-product', ProductCreateView.as_view(), name='create_product'),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('moderator/update_product/<int:pk>/', ModeratorProductUpdateView.as_view(), name='moderator_update_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('user_products/', UserProductListView.as_view(), name='user_products')
]
