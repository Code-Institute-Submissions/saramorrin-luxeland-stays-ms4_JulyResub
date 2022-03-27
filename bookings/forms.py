from .models import Reservation, UserProfile
from django import forms
from django.forms import ModelForm, CharField, TextInput



class UpdateReservation(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('check_in', 'check_out', 'guest_count', 'reservation_notes')


class EditUserProfile(forms.ModelForm):
    phone_number = CharField(widget=TextInput(attrs={'type': 'number'}))
    class Meta:
        model = UserProfile
        fields = ('name', 'email', 'phone_number')


class CreateProfile(forms.Form):
    name = forms.CharField(max_length= 50)
    email = forms.EmailField(max_length= 100)
    phone_number = forms.ImageField(max_length= 11)