from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
from phone_field import PhoneField
from django.utils.html import mark_safe, format_html
from sorl.thumbnail import get_thumbnail
from django.conf import settings

class Article(models.Model):
    
    options = (
        ("draft","Draft"),
        ("published","Published"),
        
    )
    
    title = models.CharField(max_length=255, verbose_name="Article title")
    pub_date = models.DateField( editable=True, verbose_name="Published date")
    updated = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from = "title", unique_with="pub_date__month", editable=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=options, default="draft")
    image = ResizedImageField(force_format='WEBP',quality=75,null=True, blank=True, upload_to="images/") 
    content = models.TextField()
    video = models.TextField(blank=True,null=True, default="")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("web:blog_detail", kwargs={"slug": self.slug})
    
class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    image = ResizedImageField(force_format='WEBP',quality=75,null=True, blank=True, upload_to="gallery/")
    def __str__(self):
        return self.article.title
    
    @property
    def thumbnail_preview(self):
        if self.image:
            _thumbnail = get_thumbnail(self.image,
                                   '150x150',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""
    
        
class Event(models.Model):
    title = models.CharField(max_length=255,verbose_name=_("Event name"))
    event_date = models.DateField(verbose_name=_("Event date"))
    content = models.TextField(max_length=255,verbose_name=_("Event description"))
    pub_date = models.DateField(auto_now=False, editable=True, verbose_name=_("Published date"))
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(blank=False,null=False, max_length=50)
    email = models.EmailField(blank=False,null=False,max_length=254)
    subject = models.CharField(blank=False,null=False, max_length=255)
    phone = PhoneField(blank=True,null=True, help_text="Contact phone number")
    message = models.TextField(max_length=1500)
    date = models.DateTimeField()
    
    def __str__(self):
        return self.email

class Album(models.Model):
    name = models.CharField(max_length=255)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    public = models.BooleanField(default=False)
    event_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    featured = models.BooleanField(default=False)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    image = ResizedImageField(force_format='WEBP',quality=75,null=True, blank=True, upload_to="gallery/")
    
    def __str__(self):
        return self.name
    
    @property
    def thumbnail_preview(self):
        if self.image:
            _thumbnail = get_thumbnail(self.image,
                                   '150x150',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""