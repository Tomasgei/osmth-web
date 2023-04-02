from django.shortcuts import render

# Create your views here.
def home_page(request):
    
    context = {}
    return render(request, "homepage.html",context)

def kontakt_page(request):
    
    context = {}
    return render(request, "kontakt.html",context)

def signin_page(request):
    
    context = {}
    return render(request, "signin.html",context)