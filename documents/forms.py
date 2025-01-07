from django import forms
from .models import SharedDocument

class SharedDocumentForm(forms.ModelForm):
    class Meta:
        model = SharedDocument
        fields = ['name', 'file', 'document_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'document_type': forms.Select(attrs={'class': 'form-control'}),
        }
