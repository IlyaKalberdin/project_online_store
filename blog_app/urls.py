from django.urls import path
from blog_app.apps import BlogAppConfig
from blog_app.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogAppConfig.name

urlpatterns = [
    path('create_blog/', BlogCreateView.as_view(), name='create_blog'),
    path('update_blog/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('delete_blog/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog')
]












































