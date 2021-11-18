from django.db import models
from django.utils.timezone import now

class modelReservas(models.Model):
    id_Reserva = models.AutoField(primary_key=True)
    locationParqueadero = models.CharField(max_length=250, blank=False)
    tipo_vehiculo = models.CharField(max_length=250, blank=False)
    fecha_hora_llegada = models.DateTimeField(default=now, blank=False)
    tiempo_estimado = models.DateTimeField(blank=False)