from django.shortcuts import render
from django.urls import reverse_lazy
from pytils.translit import slugify
from blog_app.models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'text', 'image', 'is_published')
    extra_context = {'title': 'Создание статьи'}
    success_url = reverse_lazy('blog_app:blog_list')

    def form_valid(self, form):
        new_blog = form.save(commit=False)
        new_blog.slug = slugify(new_blog.title)
        new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'text', 'image')
    extra_context = {'title': 'Создание статьи'}

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

        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    extra_context = {'title': 'Удаление продукта'}
    success_url = reverse_lazy('blog_app:blog_list')
