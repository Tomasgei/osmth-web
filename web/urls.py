from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    path('', views.home_page, name="home"), 
    path('kontakt/', views.kontakt_page, name="kontakt"),
    path('login/', views.signin_page, name="login"), 

   
]