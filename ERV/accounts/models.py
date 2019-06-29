
from __future__ import unicode_literals
from django.db import models

class Grupe(models.Model):
    naziv_grupe=models.CharField(max_length=128,primary_key=True)
    pocetak_rv=models.TimeField(auto_now=False)
    kraj_rv=models.TimeField(auto_now=False)
    radni_dani=models.DateField(auto_now=False)
    class Meta:
        verbose_name_plural = 'Grupe'
class Zaposleni(models.Model):
    first_name=models.CharField(max_length=128,)
    last_name=models.CharField(max_length=128,)
    pin=models.IntegerField(unique=True,blank=True,primary_key=True)
    card_number=models.IntegerField(unique=True)
    picture=models.ImageField(upload_to='profilneslike',blank=True)
    grupa=models.ForeignKey(Grupe, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Zaposleni'
class Tip_eventa(models.Model):
    event_number=models.IntegerField(primary_key=True)
    event_name=models.CharField(max_length=128)
    class Meta:
        verbose_name_plural = 'Tipovi Eventa'
class Terminal(models.Model):
    id_terminala=models.IntegerField(primary_key=True)
    naziv_terminala=models.CharField(max_length=128)
    class Meta:
        verbose_name_plural = 'Terminali'
class Event(models.Model):
    zaposleni = models.ForeignKey(Zaposleni, on_delete=models.CASCADE)
    event = models.ForeignKey(Tip_eventa, on_delete=models.CASCADE)
    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE)
    event_time=models.DateTimeField()
    event_picture=models.ImageField(upload_to='eventslike',blank=True)
    class Meta:
        verbose_name_plural = 'Eventi'