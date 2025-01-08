from django import forms
from .models import Area, Commandery

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class CommanderyForm(forms.ModelForm):
    class Meta:
        model = Commandery
        fields = ['name', 'description', 'area', 'komtur']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'area': forms.Select(attrs={'class': 'form-control'}),
            'komtur': forms.Select(attrs={'class': 'form-control'}),
        }
