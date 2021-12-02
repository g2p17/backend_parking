from django.db.models.query import QuerySet
from rest_framework                                     import generics
from rest_framework                                     import status, views
from rest_framework.response                            import Response
from parking_customers.models.parking                   import Parking
from parking_customers.serializers.parkingSerializer    import ParkingSerializer


class ParkingCreateView(generics.CreateAPIView):
    queryset           = Parking.objects.all()
    serializer_class   = ParkingSerializer
    def post(self, request, *args, **kwargs):
        '''
        Create only one parking
        '''
        serializer = ParkingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return super().post(request, *args, **kwargs)


class ParkingDetailView(generics.RetrieveAPIView):
    queryset           = Parking.objects.all()
    serializer_class   = ParkingSerializer
    def get(self, request, *args, **kwargs):
        '''
        Get only one parking
        '''
        return super().get(request, *args, **kwargs)

class ParkingUpdateView(generics.UpdateAPIView):
    queryset           = Parking.objects.all()
    serializer_class   = ParkingSerializer
    def update(self, request, *args, **kwargs):
        '''
        Update only one parking
        '''
        return super().update(request, *args, **kwargs)

class ParkingDeleteView(generics.DestroyAPIView):
    queryset           = Parking.objects.all()
    serializer_class   = ParkingSerializer
    def delete(self, request, *args, **kwargs):
        '''
        Remove only one parking
        '''
        return super().destroy(request, *args, **kwargs)

class ListParkingView(generics.ListAPIView):
    queryset           = Parking.objects.all()
    serializer_class   = ParkingSerializer
    def get_queryset(self):
        '''
        Get a parking list by admin
        '''
        queryset = Parking.objects.filter(admin_id=self.kwargs['admin_id']) 
        return queryset

class ListParking_placeView(generics.ListAPIView):
    queryset           = Parking.objects.all()
    serializer_class   = ParkingSerializer
    def get_queryset(self):
        '''
        Get a parking list by parking_place
        '''
        queryset = Parking.objects.filter(parking_place=self.kwargs['parking_place']) 
        return queryset

class ParkingsView(generics.ListAPIView):  
    queryset           = Parking.objects.all()
    serializer_class   = ParkingSerializer
    def get_queryset(self):
        '''
        Get a list of all parking lots
        '''
        queryset = Parking.objects.all()
        return queryset