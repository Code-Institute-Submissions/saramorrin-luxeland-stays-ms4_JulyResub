from django.contrib import admin
# Import Booking model from models.py
from .models import Reserve, UserProfile


admin.site.register(Reserve)

admin.site.register(UserProfile)