from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from catalog_app.forms import ProductForm, VersionForm, VersionFormSet, ModeratorProductForm
from catalog_app.models import Product, Category, Contact, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from datetime import datetime


class AuthorLoginRequiredMixin(LoginRequiredMixin):
    """ Класс-миксин, проверяющий является ли пользователь автором статьи и
        авторизован ли он"""
    def dispatch(self, request, *args, **kwargs):
        pk = kwargs['pk']
        product = Product.objects.get(id=pk)

        if request.user == product.author:
            return super().dispatch(request, *args, **kwargs)

        return self.handle_no_permission()


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Класс для создания продукта"""
    model = Product
    form_class = ProductForm
    extra_context = {'title': 'Создание продукта',
                     'categories': Category.objects.all()}

    def form_valid(self, form):
        new_product = form.save(commit=False)
        new_product.creation_date = datetime.now()
        new_product.last_modified_date = datetime.now()
        new_product.author = self.request.user
        new_product.save()

        return super().form_valid(form)


class ProductUpdateView(AuthorLoginRequiredMixin, UpdateView):
    """Класс для редактирования продукта"""
    model = Product
    form_class = ProductForm
    extra_context = {'title': 'Редактирование продукта',
                     'categories': Category.objects.all()}

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, formset=VersionFormSet, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        update_product = form.save(commit=False)
        update_product.last_modified_date = datetime.now()

        update_product.save()

        # Обработка формсета
        formset = self.get_context_data()['formset']

        if formset.is_valid():
            formset.save()
        else:
            return self.render_to_response(self.get_context_data(form=form))

        return super().form_valid(form)


class ModeratorProductUpdateView(PermissionRequiredMixin, UpdateView):
    """Класс для редактирования продукта модератором"""
    model = Product
    form_class = ModeratorProductForm
    extra_context = {'title': 'Редактирование продукта',
                     'categories': Category.objects.all()}
    permission_required = ('catalog_app.cancel_published', 'catalog_app.change_description',
                           'catalog_app.change_category')

    def form_valid(self, form):
        update_product = form.save(commit=False)
        update_product.last_modified_date = datetime.now()

        update_product.save()

        return super().form_valid(form)


class ProductListView(ListView):
    """Класс для отображения списка продуктов"""
    model = Product
    extra_context = {'title': 'Главная'}

    def get_queryset(self):
        queryset = super().get_queryset()
        user_queryset = queryset.filter(is_published=True)
        return user_queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['versions'] = Version.objects.filter(is_current_version=True)

        return context_data


class ProductDetailView(DetailView):
    """Класс для отображения подробной информации о продукте"""
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.object.name
        context_data['version'] = Version.objects.filter(product=self.object, is_current_version=True)

        return context_data


class ProductDeleteView(AuthorLoginRequiredMixin, DeleteView):
    model = Product
    extra_context = {'title': 'Удаление продукта'}
    success_url = reverse_lazy('catalog_app:home')


class UserProductListView(ListView):
    """Класс для отображения списка продуктов автора на странице мои продукты"""
    model = Product
    template_name = 'catalog_app/user_product_list.html'
    extra_context = {'title': 'Мои продукты'}

    def get_queryset(self):
        queryset = super().get_queryset()
        user_queryset = queryset.filter(author=self.request.user)
        return user_queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['published'] = self.object_list.filter(is_published=True)
        context_data['unpublished'] = self.object_list.filter(is_published=False)
        context_data['versions'] = Version.objects.filter(is_current_version=True)

        del context_data['object_list']

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
