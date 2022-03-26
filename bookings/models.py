import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Reservation Requested"), (1, "Reservation Accepted"))

class Reservation(models.Model):
    reservation_id = models.UUIDField (
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_reservations")
    check_in = models.DateField(auto_now=False)
    check_out = models.DateField(auto_now=False)
    guest_count = models.IntegerField()
    reservation_notes = models.TextField(max_length=300, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-check_in']
        

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return str(self.user)
