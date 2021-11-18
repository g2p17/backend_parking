from django.db import models


class modelEstacion(models.Model):

    parqueadero = models.CharField(unique=True,blank=False, primary_key=True, max_length=250)
    cupos_vehiculos = models.IntegerField(blank=False)
    cupos_motocicletas = models.IntegerField(blank=False)
    cupos_bicicletas = models.IntegerField(blank=False)
    cupos_esp_discapaci = models.IntegerField(blank=False)
    
    tarifa_vehiculos = models.IntegerField(blank=False)
    tarifa_motocicletas = models.IntegerField(blank=False)
    tarifa_bicicletas = models.IntegerField(blank=False)
    tarifa_esp_discapaci = models.IntegerField(blank=False)