from django.shortcuts import render, redirect, get_object_or_404
from . models import Article,Event


def home_page(request):
    articles = Article.objects.filter(status="published")[0:2]
    events = Event.objects.all()[0:3]
    
    context = {"articles":articles,
               "events":events}
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

def blog_page(request):
    article = Article.objects.filter(status="published")
    
    context = {"articles":article}
    return render(request, "blog.html",context)


