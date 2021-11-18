from rest_framework import serializers
from parqueadero import models
from parqueadero.models.estacionModel import modelEstacion

class estacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = modelEstacion
        fields = ['__all__']
