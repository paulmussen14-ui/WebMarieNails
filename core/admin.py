from django.contrib import admin
from .models import Cliente, Servicio, Cita


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre_completo", "telefono", "email", "fecha_registro")
    search_fields = ("nombre_completo", "telefono", "email")


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "duracion_minutos", "activo")
    list_filter = ("activo",)


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ("fecha", "hora", "cliente", "servicio", "tecnica", "estado")
    list_filter = ("estado", "fecha", "tecnica")
    search_fields = ("cliente__nombre_completo", "cliente__telefono")
