from parking_customers.models.parking       import Parking
from rest_framework                         import serializers

class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Parking
        fields = ['id', 'admin_id', 'parking_place', 'vehicle_slots', 'motorcycles_slots', 'bicycles_slots', 'person_with_disability_slots',
                'vehicle_price', 'motorcycles_price', 'bicycles_price', 'person_with_disability_price']

    def to_representation(self, obj):
        parking = Parking.objects.get(id=obj.id)
        return{
            'id'                            : parking.id,
            'admin_id'                      : parking.admin_id,
            'parking_place'                 : parking.parking_place,
            'vehicle_slots'                 : parking.vehicle_slots,
            'motorcycles_slots'             : parking.motorcycles_slots,
            'bicycles_slots'                : parking.bicycles_slots,
            'person_with_disability_slots'  : parking.person_with_disability_slots,
            'vehicle_price'                 : parking.vehicle_price,
            'motorcycles_price'             : parking.motorcycles_price,
            'bicycles_price'                : parking.bicycles_price,
            'person_with_disability_price'  : parking.person_with_disability_price,
        }