from django.shortcuts import render
from django.urls import reverse_lazy
from pytils.translit import slugify
from blog_app.models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


EMAIL_TO = ['ilyakalberdin@gmail.com']


class BlogCreateView(PermissionRequiredMixin, CreateView):
    model = Blog
    fields = ('title', 'text', 'image', 'is_published')
    extra_context = {'title': 'Создание статьи'}
    success_url = reverse_lazy('blog_app:blog_list')
    permission_required = 'blog_app.add_blog'

    def form_valid(self, form):
        new_blog = form.save(commit=False)
        new_blog.slug = slugify(new_blog.title)
        new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(PermissionRequiredMixin, UpdateView):
    model = Blog
    fields = ('title', 'text', 'image')
    extra_context = {'title': 'Изменение статьи'}
    permission_required = 'blog_app.change_blog'

    def form_valid(self, form):
        new_blog = form.save(commit=False)
        new_blog.slug = slugify(new_blog.title)
        new_blog.save()

        return super().form_valid(form)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        self.success_url = reverse_lazy('blog_app:blog_detail', kwargs={'pk': obj.id})
        return obj


class BlogListView(ListView):
    model = Blog
    extra_context = {'title': 'Блог'}

    def get_queryset(self):
        return self.model.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()

        self.object.send_letter(EMAIL_TO)

        return self.object


class BlogDeleteView(PermissionRequiredMixin, DeleteView):
    model = Blog
    extra_context = {'title': 'Удаление продукта'}
    success_url = reverse_lazy('blog_app:blog_list')
    permission_required = 'blog_app.delete_blog'
