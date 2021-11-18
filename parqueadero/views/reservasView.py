from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.views import APIView
from parqueadero.models.reservasModel import modelReservas
from parqueadero.serializers.reservasSerializer import reservasSerializer

class viewReservas(APIView):

    def post(self, request,*args, **kwargs):
        
        serializer_Producto = reservasSerializer(data=request.data)
        serializer_Producto.is_valid(raise_exception=True)
        serializer_Producto.save()

        return Response(data=serializer_Producto.to_representation(request.data),status=status.HTTP_201_CREATED)
        

    def get(self, request,*args,**kwargs):

        queryset = modelReservas.objects.all()
        serializer_producto = reservasSerializer(queryset, many=True)
        return Response(serializer_producto.data)