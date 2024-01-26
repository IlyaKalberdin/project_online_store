from django.shortcuts import render
from django.urls import reverse_lazy
from catalog_app.models import Product, Category, Contact
from django.views.generic import ListView, DetailView, CreateView
from datetime import datetime


class ProductCreateView(CreateView):
    """Класс для создания продукта"""
    model = Product
    fields = ('name', 'description', 'category', 'price')
    extra_context = {'title': 'Создание продукта',
                     'categories': Category.objects.all()}
    success_url = reverse_lazy('catalog_app:home')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.creation_date = datetime.now()
            new_product.last_modified_date = datetime.now()
            new_product.save()

        return super().form_valid(form)


class ProductListView(ListView):
    """Класс для отображения списка продуктов"""
    model = Product
    extra_context = {'title': 'Главная'}


class ProductDetailView(DetailView):
    """Класс для отображения подробной информации о продукте"""
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.object.name

        return context_data


def contact_page(request):
    """Функция возвращает страницу contact_page.html"""
    context = {'contact': Contact.objects.filter(id=1)[0],
               'title': 'Контакты'}

    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')

        print(f'{name}, {number}')

    return render(request, 'catalog_app/contact_page.html', context)
