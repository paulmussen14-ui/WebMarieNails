from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CitaForm
from .models import Cliente, Cita


def inicio(request):
    """
    Vista de la página principal (landing de Marie Nails).
    """
    return render(request, "index.html")


def reservar_cita(request):
    """
    Vista para crear una cita desde el formulario público.
    """
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre_completo"]
            telefono = form.cleaned_data["telefono"]
            email = form.cleaned_data["email"]
            servicio = form.cleaned_data["servicio"]
            fecha = form.cleaned_data["fecha"]
            hora = form.cleaned_data["hora"]
            tecnica = form.cleaned_data["tecnica"]

            # Obtener o crear cliente
            cliente, _ = Cliente.objects.get_or_create(
                nombre_completo=nombre,
                telefono=telefono,
                email=email,
            )

            # Crear cita
            Cita.objects.create(
                cliente=cliente,
                servicio=servicio,
                fecha=fecha,
                hora=hora,
                tecnica=tecnica,
            )

            messages.success(
                request,
                "¡Tu cita ha sido registrada! Te confirmaremos por WhatsApp o correo."
            )
            return redirect("reservar_cita")
    else:
        form = CitaForm()

    return render(request, "reservar_cita.html", {"form": form})

