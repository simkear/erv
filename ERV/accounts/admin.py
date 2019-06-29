from django.contrib import admin
from accounts.models import Zaposleni,Grupe,Event,Tip_eventa
# Register your models here.
admin.site.register(Zaposleni)
admin.site.register(Grupe)
admin.site.register(Event)
admin.site.register(Tip_eventa)

