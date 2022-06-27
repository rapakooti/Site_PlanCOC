from email.policy import default
from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from blog.views import Category, PostPlan

from accounts.forms import RegisterForm
# Create your views here.

#login.register
def login_view(request):
    StatHDV = 0
    StatMDO = 0
    StatRecrut=0
    erreur = ""

    #recupération des catégories pour les widget
    posts = PostPlan.objects.all()
    categories=Category.objects.all()
    for catego in categories:
       # posts = PostPlan.filt.all().order_by("-publication")
        if catego.name=="HDV": 
            StatHDV=posts.filter(category=catego,status='publier').count()
        if catego.name=="MDO":      
            StatMDO=posts.filter(category=catego).count()
        if catego.name=="Recrutement":   
            StatRecrut=posts.filter(category=catego).count()
    context = {
            'categories': categories,
            'StatHDV': StatHDV,
            'StatMDO': StatMDO,
            'StatRecrut': StatRecrut,
            'categories': categories,
            'erreur': erreur,
            }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None :
            login(request, user)  
            context = {
            'categories': categories,
            'erreur': erreur,
            }
            return redirect('index')  
        else :
            erreur="Erreur de connexion"
            context = {
            'categories': categories,
            'erreur': erreur,
            }
            return render(request, 'login.html',context)
        
    else: 
        return render(request, 'login.html',context)
# déconnexion de l'utilisateur

def logout_view(request):
    logout(request)
    return redirect('index')

def register_view(request):
    StatHDV = 0
    StatMDO = 0
    StatRecrut=0
       #recupération des catégories pour les widget
    posts = PostPlan.objects.all()
    categories=Category.objects.all()
    for catego in categories:
       # posts = PostPlan.filt.all().order_by("-publication")
        if catego.name=="HDV": 
            StatHDV=posts.filter(category=catego,status='publier').count()
        if catego.name=="MDO":      
            StatMDO=posts.filter(category=catego).count()
        if catego.name=="Recrutement":   
            StatRecrut=posts.filter(category=catego).count()
    
    if request.method == 'POST' :
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():

            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.set_email = user_form.cleaned_data['email']
            new_user.save()
            return redirect('login_view')
            
        else :            
            erreur=user_form.errors.as_text
            return render(request, 'register.html', {'user_form': user_form,
                                                     'categories': categories,
                                                     'erreur': erreur,
                                                     'StatHDV': StatHDV,
                                                     'StatMDO': StatMDO,
                                                     'StatRecrut': StatRecrut,
                                                     'categories': categories,})
    else :
        user_form = RegisterForm()
        return render(request, 'register.html', {'user_form': user_form,
                                                     'categories': categories,
                                                       'StatHDV': StatHDV,
                                                     'StatMDO': StatMDO,
                                                     'StatRecrut': StatRecrut,
                                                     'categories': categories,})


