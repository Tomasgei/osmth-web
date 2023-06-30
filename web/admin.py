from django.contrib import admin
from . models import Article, Event, Contact


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

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'date','name','email','phone','subject','message',)
    list_filter = ('name', 'email','phone')
    search_fields = ('name',)
