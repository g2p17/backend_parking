from rest_framework import serializers
from parqueadero import models
from parqueadero.models.reservasModel import modelReservas

class reservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = modelReservas
        fields = ['idReserva','locationParqueadero','tipo_vehiculo',
        'fecha_hora_llegada','tiempo_estimado']
