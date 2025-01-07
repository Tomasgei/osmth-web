from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'role', 'phone', 'address', 'bio']

        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'gender', 'role', 'phone', 'address', 'bio']
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
