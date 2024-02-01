from django import forms
from catalog_app.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category', 'price', 'name', 'description', 'image')
