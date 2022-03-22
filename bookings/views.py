from django.shortcuts import render
# Import Djano generic library
from django.views import generic, View
from django.views.generic import TemplateView
# Import Reservation model from models
from .models import Reservation, UserProfile
from .forms import UpdateReservation, EditUserProfile


class HomeView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "about.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class MountainLodgeView(TemplateView):
    template_name = "mountain_lodge.html"


class FirPineNestView(TemplateView):
    template_name = "fir_pine_nest.html"


class CreateProfileView(TemplateView):
    template_name = "create_profile.html"


class MakeReservationView(TemplateView):
    template_name = "make_reservation.html"