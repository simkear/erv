
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models import ImageSpecField 
from imagekit.processors import ResizeToFill
from django.conf import settings
class Preduzeca(models.Model):
    naziv_preduzeca=models.CharField(max_length=128)
    adresa_preduzeca=models.CharField(max_length=128,blank=True)
    odglice_preduzeca=models.CharField(max_length=128,blank=True)
    mail_preduzeca=models.CharField(max_length=128,unique=True,blank=True)
    brtel_preduzeca=models.CharField(max_length=128,unique=True,blank=True)
    pib_preduzeca=models.IntegerField(unique=True,primary_key=True,default=1)
    class Meta:
        verbose_name_plural = 'Preduzeca'
    def __str__(self):
        return self.naziv_preduzeca 

class Korisnik(models.Model):
     korisnik=models.OneToOneField(User,on_delete=models.CASCADE)
     picture=models.ImageField(upload_to='./zaposlenislike',blank=True)
     pib_preduzeca=models.ForeignKey(Preduzeca, on_delete=models.CASCADE,default=1)
     id_privilegija=models.IntegerField(default=1)
     image_thumbnail = ImageSpecField(source='picture',
                                 processors=[ResizeToFill(30, 30)],
                                 format='JPEG',
                                 options={'quality': 60})
     def __str__(self):
        return self.korisnik.username
     class Meta:
        verbose_name_plural = 'Korisnici'   

class Grupe(models.Model):
    naziv_grupe=models.CharField(max_length=128,primary_key=True)
    pocetak_rv=models.TimeField(auto_now=False)
    kraj_rv=models.TimeField(auto_now=False)
    radni_dani=models.DateField(auto_now=False)
    class Meta:
        verbose_name_plural = 'Grupe'
    def __str__(self):
        return self.naziv_grupe 

class Zaposleni(models.Model):
    first_name=models.CharField('Ime',max_length=128,)
    last_name=models.CharField('Prezime',max_length=128,)
    pin=models.IntegerField('PIN',unique=True,blank=True,primary_key=True)
    card_number=models.IntegerField('Broj RFID Kartice',unique=True)
    picture=models.ImageField('Fotografija',upload_to='./zaposlenislike',blank=True)
    grupa=models.ForeignKey(Grupe, on_delete=models.CASCADE)
    pib_preduzeca=models.ForeignKey(Preduzeca, on_delete=models.CASCADE)
    created=models.DateTimeField('Kreiran',auto_now=False, auto_now_add=True,null=True)
    modified=models.DateTimeField('Modifikovan',auto_now=True, auto_now_add=False,null=True)
    creator=models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Zaposleni'
    def __str__(self):
        return self.first_name + " " + self.last_name   

class Tip_eventa(models.Model):
    event_number=models.IntegerField(primary_key=True)
    event_name=models.CharField(max_length=128)
    class Meta:
        verbose_name_plural = 'Tipovi Eventa'
    def __str__(self):
        return self.event_name 

class Terminal(models.Model):
    id_terminala=models.IntegerField(primary_key=True)
    naziv_terminala=models.CharField(max_length=128)
    pib_preduzeca=models.ForeignKey(Preduzeca, on_delete=models.CASCADE,default=1)
    class Meta:
        verbose_name_plural = 'Terminali'
    def __str__(self):
        return self.naziv_terminala

class Event(models.Model):
    zaposleni = models.ForeignKey(Zaposleni, on_delete=models.CASCADE)
    event = models.ForeignKey(Tip_eventa, on_delete=models.CASCADE)
    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE)
    event_time=models.DateTimeField()
    event_picture=models.ImageField(upload_to='eventslike',blank=True)
    class Meta:
        verbose_name_plural = 'Eventi'
     
class Time(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    start_month = models.DateField()
    end_month = models.DateField()
    start_year = models.DateField()
    end_year = models.DateField()
    pub_date = models.CharField('date published',max_length=24)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/dpp_test/event/' + str(self.pk)            