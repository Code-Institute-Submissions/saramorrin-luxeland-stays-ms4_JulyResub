from .models import Reservation, UserProfile
from django import forms
from django.forms import ModelForm


class UpdateReservation(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('__all__')


class EditUserProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('__all__')