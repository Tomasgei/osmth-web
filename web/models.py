from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from django.contrib.auth.models import User


class Article(models.Model):
    
    options = (
        ("draft","Draft"),
        ("published","Published"),
        
    )
    
    title = models.CharField(max_length=255)
    pub_date = models.DateField(auto_now=True, editable=True, verbose_name="Published date")
    updated = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from = "title", unique_with="pub_date__month")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=options, default="draft")
    image = models.ImageField(null=True, blank=True, upload_to="images/") 
    content = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("web:blog_detail", kwargs={"slug": self.slug})