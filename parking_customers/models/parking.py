from django.db                   import models

class Parking(models.Model):
    '''
        Manage PositiveSmallIntegerField for efficiency memory cause our project don't need negative numbers
    '''
    id                              = models.AutoField(primary_key=True)
    admin_id                        = models.CharField(max_length = 50)
    parking_place                   = models.CharField(max_length = 50)
    vehicle_slots                   = models.PositiveSmallIntegerField(default=0)
    motorcycles_slots               = models.PositiveSmallIntegerField(default=0)
    bicycles_slots                  = models.PositiveSmallIntegerField(default=0)
    person_with_disability_slots    = models.PositiveSmallIntegerField(default=0)
    vehicle_price                   = models.PositiveSmallIntegerField(default=0)
    motorcycles_price               = models.PositiveSmallIntegerField(default=0)
    bicycles_price                  = models.PositiveSmallIntegerField(default=0)
    person_with_disability_price    = models.PositiveSmallIntegerField(default=0)