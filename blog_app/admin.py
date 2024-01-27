from django.contrib import admin
from blog_app.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'creation_date', 'count_views', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title', 'text',)
