from django.db                   import models

class Parking(models.Model):
    id                              = models.AutoField(primary_key=True)
    admin_id                        = models.CharField(max_length = 50)
    parking_place                   = models.CharField(max_length = 50)
    vehicle_slots                   = models.IntegerField(default=0)
    motorcycles_slots               = models.IntegerField(default=0)
    bicycles_slots                  = models.IntegerField(default=0)
    person_with_disability_slots    = models.IntegerField(default=0)
    vehicle_price                   = models.IntegerField(default=0)
    motorcycles_price               = models.IntegerField(default=0)
    bicycles_price                  = models.IntegerField(default=0)
    person_with_disability_price    = models.IntegerField(default=0)