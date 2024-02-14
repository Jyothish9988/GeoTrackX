from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout

def homepage(request):
    return render(request, 'home/index.html')

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CreateUserForm()

    context = {'registerform': form}
    return render(request, 'home/register.html', context=context)

def user_login(request):  # Renamed from 'login' to 'user_login'
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("dashboard")

    else:
        form = LoginForm()

    context = {'loginform': form}
    return render(request, 'home/login.html', context=context)

@login_required(login_url='/user_login')  # Adjusted login URL to 'user_login'
def user_logout(request):
    logout(request)
    return redirect("")

@login_required(login_url='/user_login')  # Adjusted login URL to 'user_login'
def dashboard(request):
    return render(request, 'home/dashboard.html')
