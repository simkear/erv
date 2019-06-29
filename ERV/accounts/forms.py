from django import forms
from django.contrib.auth import authenticate,get_user_model
from accounts.models import Zaposleni,Grupe
User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Ovaj korisnik ne postoji')
            if not user.check_password(password):
                raise forms.ValidationError('Pogresna lozinka')
            if not user.is_active:
                raise forms.ValidationError('Ovaj korisnik nije aktivan')
        return super(UserLoginForm, self).clean(*args, **kwargs)

class NoviZaposleniForma(forms.ModelForm):
    class Meta:
        model = Zaposleni
        fields = '__all__'
class NovaGrupaForma(forms.ModelForm):
    class Meta:
        model = Grupe
        fields = '__all__'