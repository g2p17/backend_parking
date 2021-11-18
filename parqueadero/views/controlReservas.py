from rest_framework import generics
from parqueadero.models.reservasModel import modelReservas
from parqueadero.serializers.reservasSerializer import reservasSerializer

class getReserva(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        self.queryset= modelReservas.objects.all()
        self.serializer_class = reservasSerializer
        return super().get(request, *args, **kwargs)

class updateReserva(generics.RetrieveUpdateDestroyAPIView):
    queryset = modelReservas.objects.all()
    serializer_class   = reservasSerializer
    
    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class DeleteReserva(generics.DestroyAPIView):
    queryset           = modelReservas.objects.all()
    serializer_class   = reservasSerializer
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)