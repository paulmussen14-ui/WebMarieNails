from django import forms
from .models import Servicio


class CitaForm(forms.Form):
    nombre_completo = forms.CharField(max_length=150, label="Nombre completo")
    telefono = forms.CharField(max_length=20, label="Teléfono / WhatsApp")
    email = forms.EmailField(label="Correo electrónico")
    servicio = forms.ModelChoiceField(
        queryset=Servicio.objects.filter(activo=True),
        label="Servicio"
    )
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Fecha"
    )
    hora = forms.TimeField(
        widget=forms.TimeInput(attrs={"type": "time"}),
        label="Hora"
    )
    tecnica = forms.CharField(
        max_length=100,
        required=False,
        label="Técnica (opcional)"
    )
