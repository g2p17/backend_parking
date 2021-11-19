from django.db.models.query import QuerySet
from rest_framework                                     import generics
from rest_framework                                     import status, views
from rest_framework.response                            import Response
from parking_customers.models.parking                   import Parking
from parking_customers.serializers.parkingSerializer    import ParkingSerializer

class ParkingCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        print(kwargs)
        serializer = ParkingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

class ParkingDetailView(generics.RetrieveAPIView):
    queryset           = Parking.objects.all()
    serializer_class   = ParkingSerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ParkingUpdateView(generics.UpdateAPIView):
    queryset           = Parking.objects.all()
    serializer_class   = ParkingSerializer
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class UserDeleteView(generics.DestroyAPIView):
    queryset           = Parking.objects.all()
    serializer_class   = ParkingSerializer
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ListParkingView(generics.ListAPIView):
    queryset           = Parking.objects.all()
    serializer_class   = ParkingSerializer
    
    def get_queryset(self):
        queryset = Parking.objects.filter(admin_id=self.kwargs['admin_id']) 
        #queryset = Parking.objects.filter(origin_account_id=self.kwargs['account']) id=account.user_id
        return queryset

