from django.shortcuts import render, get_object_or_404, reverse, redirect
# Import Djano generic library
from django.views import generic, View
from django.views.generic import TemplateView, DeleteView
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


class EditReservationView(TemplateView):
    template_name = "edit_reservation.html"


class CreateProfileView(TemplateView):
    template_name = "create_profile.html"

    def get (self, request, *args, **kwargs):
        return render(
            request,
            "create_profile.html",
        )

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone_number")

        CreateUserProfile = UserProfile.objects.create(
            name=name,
            email=email,
            phone_number=phone,
            user=request.user

        )

        CreateUserProfile.save()

        return redirect(reverse('home'))

# Make reservation view
class MakeReservationView(TemplateView):
    template_name = "make_reservation.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "make_reservation.html"
        )

    def post(self, request):
        check_in_date = request.POST.get("check_in_date")
        check_out_date = request.POST.get("check_out_date")
        number_of_guests = request.POST.get("number_of_guests")
        notes = request.POST.get("notes")

        make_reservation = Reservation.objects.create(
            check_in=check_in_date,
            check_out=check_out_date,
            guest_count=number_of_guests,
            user=request.user,
            reservation_notes=notes
        )

        make_reservation.save()

        return redirect(reverse('edit_reservation'))
