from rest_framework import generics
from parqueadero.models.estacionModel import modelEstacion
from parqueadero.serializers.estacionSerializer import estacionSerializer

class getEstacion(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        self.queryset= modelEstacion.objects.all()
        self.serializer_class = estacionSerializer
        return super().get(request, *args, **kwargs)

class updateEstacion(generics.RetrieveUpdateDestroyAPIView):
    queryset = modelEstacion.objects.all()
    serializer_class   = estacionSerializer
    
    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class DeleteEstacion(generics.DestroyAPIView):
    queryset           = modelEstacion.objects.all()
    serializer_class   = estacionSerializer
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)