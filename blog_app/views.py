from django.shortcuts import render
from django.urls import reverse_lazy
from blog_app.models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class BlogListView(ListView):
    model = Blog
    extra_context = {'title': 'Блог'}
