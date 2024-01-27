from django.urls import path
from blog_app.apps import BlogAppConfig
from blog_app.views import BlogListView

app_name = BlogAppConfig.name

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog_list')
]












































