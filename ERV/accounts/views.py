from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, UpdateView
from django.http import HttpResponseRedirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login_required
from .forms import UserLoginForm
from accounts.forms import NoviZaposleniForma,NovaGrupaForma,TimeForm
from accounts.models import Time,Zaposleni,Korisnik

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
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
@login_required    
def zaposleni(request):
    pib = request.user.korisnik.pib_preduzeca
    form = NoviZaposleniForma()
    form1 = Zaposleni.objects.filter(pib_preduzeca=pib)
    if request.method == "POST":
        form = NoviZaposleniForma(request.POST, request.FILES)
        if form.is_valid():
            i=form.save(commit=False)
            i.creator=request.user
            i.pib_preduzeca=pib
            i.save()

            return redirect('/zaposleni')
        else:
            print('Forma nije ispravna')
    return render(request,'zaposleni.html',{'form':form,'form1':form1,'pib':pib})

@login_required    
def prikaz_zaposleni(request):
    form = NoviZaposleniForma()
    if request.method == "POST":
        form = NoviZaposleniForma(request.POST, request.FILES)
        if form.is_valid():
            form.pib_preduzeca=request.user.korisnik.pib_preduzeca
            form.save(commit=True)
            publish = form.save(commit=False)
            publish.student = request.user
            publish.save() 

            return redirect('/zaposleni')
        else:
            print('Forma nije ispravna')
    return render(request,'zaposleni.html',{'form1':form})

@login_required
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


class Bootstrap3_UpdateView(UpdateView):
    template_name = 'accounts/bootstrap3/model-form.html'
    model = Time
    form_class = TimeForm


class Bootstrap4_UpdateView(UpdateView):
    template_name = 'accounts/bootstrap4/model-form.html'
    model = Time
form_class = TimeForm