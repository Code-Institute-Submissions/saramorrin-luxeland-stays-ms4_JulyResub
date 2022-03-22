from django.shortcuts import render
# Import Djano generic library
from django.views import generic, View
from django.views.generic import TemplateView
# Import Reservation model from models
from .models import Reservation, UserProfile
from .forms import UpdateReservation, EditUserProfile


class HomeView(TemplateView):
    template_name = "index.html"
