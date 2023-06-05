from django.contrib import admin
from . models import Article, Event


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'pub_date','updated','status')
    list_filter = ('author', 'pub_date','status')
    search_fields = ('author', 'title')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'event_date','pub_date','updated')
    list_filter = ('title', 'event_date','pub_date')
    search_fields = ('title',)
