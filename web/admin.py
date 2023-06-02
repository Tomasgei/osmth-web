from django.contrib import admin
from . models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'pub_date','updated','status')
    list_filter = ('author', 'pub_date','status')
    search_fields = ('author', 'title')

