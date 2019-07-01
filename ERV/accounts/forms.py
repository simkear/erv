from django import forms
from django.contrib.auth import authenticate,get_user_model
from accounts.models import Zaposleni,Grupe,Time
from bootstrap_datepicker_plus import DatePickerInput,TimePickerInput
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
                raise forms.ValidationError('Pogresno korisnicko ime ili lozinka')
        return super(UserLoginForm, self).clean(*args, **kwargs)

class NoviZaposleniForma(forms.ModelForm):
    class Meta:
        model = Zaposleni
        exclude = ['pib_preduzeca','created','modified','creator',]
        
class NovaGrupaForma(forms.ModelForm):
    class Meta:
        model = Grupe
        fields = '__all__'

class TimeForm(forms.ModelForm):
     class Meta:
         model = Time
         fields = ['name','pub_date', 'start_date', 'end_date', 'start_time', 'end_time']
         widgets = {
             'pub_date': DatePickerInput(
                 options={
                     "format": "DD/MM/YYYY",
                     "locale": "sr",
                 }
             ),
             'start_date':DatePickerInput().start_of('event days'),
             'end_date':DatePickerInput().end_of('event days'),
             'start_time':TimePickerInput().start_of('party time'),
             'end_time':TimePickerInput().end_of('party time'),
         }