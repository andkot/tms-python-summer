from django.contrib import admin
from blog.models import Article


class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'author_name', 'author')
    search_fields = ('title', 'description')
    list_display = ('title', 'short_description', 'author_name', 'author')


admin.site.register(Article, ArticleAdmin)
