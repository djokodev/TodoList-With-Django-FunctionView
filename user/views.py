from django.shortcuts import render, redirect
from user.forms import CustomUserForm, CustomLoginForm
from django.contrib.auth import login, logout, authenticate, get_user_model

def register(request):
    form = CustomUserForm()
    errors = ""
    user = None

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            User = get_user_model()
            username = form.cleaned_data['username']
            if User.objects.filter(username=username):
               errors = "Un utilisateur avec ce nom existe déjà !"
            else:
                user = form.save()
                login(request, user)
                return redirect('home')
        else:
            errors = "Nom d'utilisateur ou mot de passe incorrecte !"

    return render(request, "user/register.html", {'form':form, "errors":errors})

def login_user(request):
    form = CustomLoginForm()
    errors = ""

    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                errors = "Nom d'utilisateur ou mot de passe incorrect."
        else:
            form = CustomLoginForm()
    return render(request, "user/login.html", {"form":form, "errors":errors})

