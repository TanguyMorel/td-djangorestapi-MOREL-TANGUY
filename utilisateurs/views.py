# utilisateurs/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# utilisateurs/views.py
from django.shortcuts import render

def landing_page(request):
    return render(request, 'utilisateurs/landing_page.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Création d'un profil utilisateur associé si nécessaire
            # Exemple: profile = UserProfile(user=user)
            # profile.save()
            login(request, user)
            return redirect('signin')  # Rediriger vers la page d'accueil après inscription
    else:
        form = UserCreationForm()
    return render(request, 'utilisateurs/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Rediriger vers la page d'accueil après connexion
    else:
        form = AuthenticationForm()
    return render(request, 'utilisateurs/signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('home')  # Rediriger vers la page d'accueil après déconnexion
