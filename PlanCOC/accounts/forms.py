from django import forms    
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label="Username", max_length=250, help_text="", required=True,
    widget=forms.TextInput(attrs={'class': "form-control", "id":"username", "name":"username", "placeholder":"nom d'utilisateur"}))

    first_name = forms.CharField(label="Prenom", max_length=250, help_text="", required=True,
    widget=forms.TextInput(attrs={'class': "form-control", "id":"Prenom", "name":"Prenom", "placeholder":"Prénom"}))
    last_name = forms.CharField(label="Prenom", max_length=250, help_text="", required=True,
    widget=forms.TextInput(attrs={'class': "form-control", "id":"Nom", "name":"Nom", "placeholder":"Nom"}))
    email = forms.EmailField(label="Email", max_length=250, help_text="", required=True,
    widget=forms.TextInput(attrs={'class': "form-control", "id":"Email", "name":"Email", "placeholder":"Adresse de messagerie"}))
    last_name = forms.EmailField(label="Email", max_length=250, help_text="", required=True,
    widget=forms.TextInput(attrs={'class': "form-control", "id":"Email", "name":"Email", "placeholder":"Adresse de messagerie"}))



    class Meta:
        model = User
        fields = ('username', 'password','first_name', 'last_name', 'email')