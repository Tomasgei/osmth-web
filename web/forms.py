from django import forms
from django.core.validators import EmailValidator
from django.contrib.auth.forms import AuthenticationForm


class ContactForm(forms.Form):
    name = forms.CharField(label="Jméno", max_length=155, required=True, widget=forms.TextInput(attrs={"placeholder":"Vaše celé jméno","class":"form-control","id":"name"}))
    email = forms.CharField(required=True, validators=[EmailValidator()],widget=forms.EmailInput(attrs={"placeholder":"Vyplňte prosím vaší emailovou adresu","class":"form-control","id":"emailAddress"}))
    phone = forms.CharField(label="Telefon", max_length=15, widget=forms.TextInput(attrs={"placeholder":"Telefonní kontakt na vás","class":"form-control","id":"phone"}))
    subject = forms.CharField(label="Předmět", max_length=155, required=True, widget=forms.TextInput(attrs={"placeholder":"Prosím napište předmět zprávy","class":"form-control","id":"subject"}))
    message = forms.CharField(label=False, widget=forms.Textarea(attrs={"placeholder":"Zde napište svou zprávu","class":"form-control","style":"height: 10rem;"    }))
     
    

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Uživatelské jméno'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Heslo'
        })
    )
