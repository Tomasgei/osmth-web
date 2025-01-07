from django.contrib import admin
from .models import SharedDocument

@admin.register(SharedDocument)
class SharedDocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'document_type', 'uploaded_at')
    search_fields = ('name',)
    list_filter = ('document_type',)
    ordering = ('-uploaded_at',)

