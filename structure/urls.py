from django.urls import path
from . import views

urlpatterns = [
    path('areas/', views.area_list, name='area_list'),
    path('areas/add/', views.add_area, name='add_area'),
    path('areas/<int:area_id>/edit/', views.edit_area, name='edit_area'),
    path('commandery/', views.commandery_detail, name='commandery_detail'),
]
