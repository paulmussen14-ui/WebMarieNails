from django.db import models


class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_completo


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    duracion_minutos = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Cita(models.Model):

    ESTADOS = [
        ("PENDIENTE", "Pendiente"),
        ("CONFIRMADA", "Confirmada"),
        ("ATENDIDA", "Atendida"),
        ("CANCELADA", "Cancelada"),
    ]

    fecha = models.DateField()
    hora = models.TimeField()

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)

    tecnica = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Nombre de la técnica que atiende (si aplica)"
    )

    estado = models.CharField(
        max_length=12,
        choices=ESTADOS,
        default="PENDIENTE"
    )

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.cliente}"





