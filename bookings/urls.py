from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('mountain_lodge/', views.MountainLodgeView.as_view(), name='mountain_lodge'),
    path('fir_pine_nest/', views.FirPineNestView.as_view(), name='fir_pine_nest'),
    path('create_profile/', views.CreateProfileView.as_view(), name='create_profile'), 
    path('make_reservation/', views.MakeReservationView.as_view(), name='make_reservation'), 
]