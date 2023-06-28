from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from . models import Article,Event
from . forms import ContactForm


def home_page(request):
    articles = Article.objects.filter(status="published")[0:2]
    events = Event.objects.all()[0:3]
    
    context = {"articles":articles,
               "events":events}
    return render(request, "homepage.html",context)

def kontakt_page(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            try:
                send_mail( subject= subject,
                          message=message, from_email=email, recipient_list=["x.zem@seznam.cz","geissler.tomas@gmail.com","prioratus@osmth.cz"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("web:success")
        
    context = {"form":form}
    return render(request, "kontakt.html",context)

def success_view(request):
    return HttpResponse("Succes! Thank you for your message.")


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


