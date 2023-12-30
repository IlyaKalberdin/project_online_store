from django.urls import path
from catalog_app.views import home_page, contact_page

urlpatterns = [
    path('', home_page),
    path('contacts', contact_page)
]
