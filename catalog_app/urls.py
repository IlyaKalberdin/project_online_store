from django.urls import path
from catalog_app.views import ProductListView, contact_page, ProductDetailView, ProductCreateView
from catalog_app.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts', contact_page, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create-product', ProductCreateView.as_view(), name='create_product')
]
