from django.shortcuts import render
from django.urls import reverse_lazy
from pytils.translit import slugify
from blog_app.models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'text', 'image')
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
    success_url = reverse_lazy('blog_app:blog_list')

    def form_valid(self, form):
        new_blog = form.save(commit=False)
        new_blog.slug = slugify(new_blog.title)
        new_blog.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    extra_context = {'title': 'Блог'}


class BlogDetailView(DetailView):
    model = Blog


class BlogDeleteView(DeleteView):
    model = Blog
    extra_context = {'title': 'Удаление продукта'}
    success_url = reverse_lazy('blog_app:blog_list')
