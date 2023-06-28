from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    path('', views.home_page, name="home"),
    path('blog', views.blog_page, name="blog"),
    path('blog/<slug:slug>', views.blog_detail_page, name="blog_detail"), 
    path('kontakt/', views.kontakt_page, name="kontakt"),
    path("succes/",views.success_view, name="success"),
    path('login/', views.signin_page, name="login"), 
]