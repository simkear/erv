from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm
from accounts.forms import NoviZaposleniForma,NovaGrupaForma

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect('/')
def zaposleni(request):
    form = NoviZaposleniForma()
    if request.method == "POST":
        form = NoviZaposleniForma(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
        else:
            print('Forma nije ispravna')
    return render(request,'zaposleni.html',{'form':form})

def grupe(request):
    form = NovaGrupaForma()
    if request.method == "POST":
        form = NovaGrupaForma(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
        else:
            print('Forma nije ispravna')
    return render(request,'grupe.html',{'form':form}) 