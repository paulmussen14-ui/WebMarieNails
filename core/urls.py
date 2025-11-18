
from django.urls import path
from .views import inicio, reservar_cita

urlpatterns = [
    path("", inicio, name="inicio"),
    path("reservar/", reservar_cita, name="reservar_cita"),
]
