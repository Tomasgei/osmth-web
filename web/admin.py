from django.contrib import admin
from . models import Article, Event, Contact,ArticleImage, Album, Image


class ArticleImageAdmin(admin.StackedInline):
    model=ArticleImage
    readonly_fields = ('thumbnail_preview',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleImageAdmin]

    list_display = ('author', 'title', 'pub_date','updated','status')
    list_filter = ('author', 'pub_date','status')
    search_fields = ('author', 'title')

    class Meta:
        model = Article
            
#@admin.register(ArticleImage)
#class ArticleImageAdmin(admin.ModelAdmin):
#    readonly_fields = ('thumbnail_preview',)
#    pass
class ImageAdmin(admin.StackedInline):
    model =Image
    readonly_fields = ('thumbnail_preview',)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]
    list_display = ( 'name','event_date',"article","public")
    list_filter = ('name', 'event_date','public')
    search_fields = ('name',)
    
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('thumbnail_preview',)
    list_display = ( "thumbnail_preview",'featured','name',"image","album",)
    list_filter = ("album", 'featured',)
    search_fields = ('name',"album",)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True


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
    
