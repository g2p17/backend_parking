from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.views import APIView
from parqueadero.models.estacionModel import modelEstacion
from parqueadero.serializers.estacionSerializer import estacionSerializer

class viewEstacion(APIView):

    def post(self, request,*args, **kwargs):
        
        serializer_Producto = estacionSerializer(data=request.data)
        serializer_Producto.is_valid(raise_exception=True)
        serializer_Producto.save()

        return Response(data=serializer_Producto.to_representation(request.data),status=status.HTTP_201_CREATED)
        

    def get(self, request,*args,**kwargs):

        queryset = modelEstacion.objects.all()
        serializer_producto = estacionSerializer(queryset, many=True)
        return Response(serializer_producto.data)