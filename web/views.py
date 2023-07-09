from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from . models import Article,Event,Contact,ArticleImage,Album,Image
from . forms import ContactForm
from django.utils import timezone
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from django.db.models import Q


def home_page(request):
    articles = Article.objects.filter(status="published")[0:2]
    events = Event.objects.all()[0:3]
    photos = Image.objects.filter(featured=True)[0:6]
    
    context = {"articles":articles,
               "events":events,
               "photos":photos,}
    return render(request, "homepage.html",context)

def kontakt_page(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            
            contact = Contact(
                    name = name,
                    email = email,
                    phone = phone,
                    subject = subject,
                    message = message,
                    date = timezone.now()
            )
            contact.save()
            messages.success(request, 'Vaše zpráva byla úspěšně odeslána.Odpovíme Vám v nejbližšší možné době')
            try:
                html_message = render_to_string("../templates/email_templates/contact_reply.html", {"name":name,
                                                                                                    "email":email,
                                                                                                    "phone":phone,
                                                                                                    "message":message,
                                                                                                    })
                plain_message = strip_tags(html_message)
                to = ["x.zem@seznam.cz","geissler.tomas@gmail.com","prioratus@osmth.cz"]
                send_mail( subject= subject,
                          message=plain_message, from_email=email, recipient_list=to,html_message=html_message)
                
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("http://osmth.cz/kontakt/#kontakt")
        
    context = {"form":form}
    return render(request, "kontakt.html",context)

def success_view(request):
    return HttpResponse("Succes! Thank you for your message.")


def signin_page(request):
    
    context = {}
    return render(request, "signin.html",context)

def blog_detail_page(request,slug):
    article = get_object_or_404(Article, slug=slug)
    photos = ArticleImage.objects.filter(article=article)
    articles = Article.objects.filter(~Q(slug=slug),status="published")[0:3]
    #album = Album.objects.get(article=article)
    #img = Image.objects.filter(album=album)
    context = {"article":article,
               "photos":photos,
               "articles":articles,
                 }
    return render(request, "blog_detail.html",context)

def blog_page(request):
    article = Article.objects.filter(status="published")
    
    context = {"articles":article}
    return render(request, "blog.html",context)


