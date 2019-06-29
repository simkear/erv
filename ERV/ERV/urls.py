
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import home,tables,forget,charts,alarmi,alarmiGrupa
from accounts.views import login_view,logout_view,zaposleni,grupe
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('accounts/login/', login_view),
    path('accounts/logout/', logout_view),
    path('tables/', tables),
    path('forget/', forget),
    path('charts/', charts),
    path('zaposleni/', zaposleni),
    path('grupe/', grupe)
    
]
