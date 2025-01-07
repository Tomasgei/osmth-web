from django.urls import path
from . import views

urlpatterns = [
    path('documents/', views.shared_documents_list, name='shared_documents_list'),
    path('documents/upload/', views.upload_shared_document, name='upload_shared_document'),
]
