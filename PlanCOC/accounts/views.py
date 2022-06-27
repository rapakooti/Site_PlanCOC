from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from blog.views import Category

from accounts.forms import RegisterForm
# Create your views here.

#login.register
def login(request):
    categories=Category.objects.all()
    context = {
        'categories': categories
    }
    if request.method == 'POST':
        if 'username' not in  request.POST or 'password' not in request.POST :
            erreur="Veuillez entrer un Pseudo et un mot de passe correct"
            return render( request, 'login.html', {'erreur': erreur})
        else :
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

        if user is not None :
            erreur="Erreur d'authentification"
            return render( request, 'login.html', {'erreur': erreur,
                                                    'categories': categories})
        else :
            return redirect('index')
        
    else: 
        return render(request, 'login.html', {'categories': categories})
# déconnexion de l'utilisateur

def logout_view(request):
    logout(request)
    return redirect('index')

def register_view(request):
    categories=Category.objects.all()
    context = {
        'categories': categories
    }
    if request.method == 'POST' :
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_passeword(user_form.clean_data['password'])
            new_user.save()
            return redirect('login')
        else :
            return render(request, 'register.html', {'user_form': user_form})
    else :
        user_form = RegisterForm()
        return render(request, 'register.html', {'user_form': user_form})