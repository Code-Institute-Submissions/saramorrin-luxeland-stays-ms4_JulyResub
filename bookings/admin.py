from django.contrib import admin
# Import Booking model from models.py
from .models import Reservation, UserProfile


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'check_in', 'check_out', 'guest_count')
    search_fields = ('user', 'check_in')
    actions = ['approve_reservation']

    def approve_reservation(self, queryset):
        queryset.update(approve_reservation=True)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name', 'email')