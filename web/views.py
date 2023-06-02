from django.shortcuts import render, redirect, get_object_or_404
from . models import Article


def home_page(request):
    articles = Article.objects.filter(status="published")[0:2]
    
    context = {"articles":articles}
    return render(request, "homepage.html",context)

def kontakt_page(request):
    
    context = {}
    return render(request, "kontakt.html",context)

def signin_page(request):
    
    context = {}
    return render(request, "signin.html",context)

def blog_detail_page(request,slug):
    article = get_object_or_404(Article, slug=slug)
    
    context = {"article":article}
    return render(request, "blog_detail.html",context)


