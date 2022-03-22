from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Reservation Requested"), (1, "Reservation Accepted"))

class Reservation(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_bookings")
    check_in = models.DateField(auto_now=False)
    check_out = models.DateField(auto_now=False)
    guest_count = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-check_in']
        

class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    notes = models.TextField()

    def __str__(self):
        return str(self.user)
