from django import forms
from catalog_app.models import Product, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category', 'price', 'name', 'description', 'image', 'is_published')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

            if field_name == 'is_published':
                field.widget.attrs['class'] = 'form-check'

    def clean_name(self):
        cleaned_name = self.cleaned_data.get('name')

        name_exception_words = self.get_clean_set(cleaned_name)

        if name_exception_words:
            name_exception_words = ', '.join(name_exception_words)
            raise forms.ValidationError(f'Нельзя использовать следующие слова: {name_exception_words}')

        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data.get('description')

        description_exception_words = self.get_clean_set(cleaned_description)

        if description_exception_words:
            description_exception_words = ', '.join(description_exception_words)
            raise forms.ValidationError(f'Нельзя использовать следущие слова: {description_exception_words}')

        return cleaned_description

    @staticmethod
    def get_clean_set(string):
        """Метод принимает строку и возвращает множество со словами исключениями
        из этой строки"""
        translate_dict = {ord(','): None, ord('-'): None, ord(':'): None,
                          ord(';'): None, ord('.'): None}

        exception_words = {'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                           'бесплатно', 'обман', 'полиция', 'радар'}

        string = string.lower()
        string = string.translate(translate_dict)
        string_set = set(string.split())

        string_exception_words = exception_words.intersection(string_set)

        return string_exception_words


class ModeratorProductForm(ProductForm):
    """Форма для редактирования продукта модераторами"""

    class Meta:
        model = Product
        fields = ('category', 'description', 'is_published')


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == 'is_current_version':
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class VersionFormSet(forms.BaseInlineFormSet):

    def clean(self):
        cleaned_forms = self.cleaned_data

        list_true = []
        for cleaned_form in cleaned_forms:
            list_true.append(cleaned_form.get('is_current_version'))

        if list_true.count(True) > 1:
            raise forms.ValidationError('Продукт может иметь только одну текущую версию.')

        super().clean()
