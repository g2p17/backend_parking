from rest_framework import serializers
from parqueadero.models.manageUser import modelUser

class LoginResgistro_serializer(serializers.ModelSerializer):

    class Meta:
        model = modelUser
        fields = ['id','name','email','placa_vehiculo','telephone','password','presentar_movilidad','type_vehiculo']

        def to_representation(self,obj):
            toSearchUser = modelUser.objects.get(id=obj.id)
            return {
                'id': toSearchUser.id,
                'telephone': toSearchUser.telephone,
                'name': toSearchUser.name,
                'email': toSearchUser.email,
                'placa_vehiculo' : toSearchUser.placa_vehiculo
            }
        