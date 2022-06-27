from django import forms    
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User=get_user_model()

class RegisterForm(forms.ModelForm):
    
    username = forms.CharField(label="Username", max_length=250, help_text="", required=True,
    widget=forms.TextInput(attrs={'class': "form-control border-danger ", "id":"username", "name":"username", "placeholder":"Nom d'utilisateur"}))

    first_name = forms.CharField(label="Prenom", max_length=250,min_length=4, help_text="", required=True,
    widget=forms.TextInput(attrs={'class': "form-control border-danger ", "id":"Prenom", "name":"Prenom", "placeholder":"Prénom"}))
    last_name = forms.CharField(label="nom", max_length=250,min_length=4, help_text="", required=True,
    widget=forms.TextInput(attrs={'class': "form-control border-danger ", "id":"Nom", "name":"Nom", "placeholder":"Nom"}))
    email = forms.EmailField(label="Email", max_length=250, help_text="", required=True,
    widget=forms.TextInput(attrs={'class': "form-control border-danger ", "id":"Email", "name":"Email", "placeholder":"Adresse de messagerie"}))
    password = forms.CharField(label="password", max_length=250,min_length=8, help_text="", required=True,
    widget=forms.TextInput(attrs={"type":"password",'class': "form-control border-danger ", "id":"password", "name":"password", "placeholder":"Mot de passe"}))
    confirmPassword = forms.CharField( label="confirmPassword", max_length=250,min_length=8, help_text="", required=True,
    widget=forms.TextInput(attrs={"type":"password",'class': "form-control border-danger ", "id":"confirmPassword", "name":"confirmPassword", "placeholder":"Confirmer le mot de passe"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user_count=User.objects.filter(email=email).count()
        if user_count>0 :
            raise forms.ValidationError("Ce mail est déjà utilisé par un autre utilisateur")
        else :
            return email  
       
    def clean_password(self):
        #cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirmPassword')
        if password != password2:
           # msg="Les deux mots de passe ne sont pas identiques"
            #self._errors['password'] = self.error_class([msg])
         #  self.add_error('password', "oupps ca marche pas")
            raise forms.ValidationError("Les mot de passe ne sont pas identiques")
          
        return password    
   


    class Meta:
        model = User
        fields = ('username', 'password','first_name', 'last_name', 'email')