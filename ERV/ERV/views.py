from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from accounts.models import Korisnik


@login_required
def home(request):
    context={'korisnik': Korisnik.objects.all()}
    return render(request, "index.html", context, {})
@login_required
def tables(request):
    return render(request, "tables.html", {})
@login_required
def charts(request):
    return render(request, "charts.html", {})
@login_required
def alarmi(request):
    return render(request, "alarmi.html", {})
@login_required
def alarmiGrupa(request):
    return render(request, "alarmgi.html", {})
@login_required
def forget(request):
    return render(request, "forget-password.html", {})
