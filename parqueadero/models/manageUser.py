from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):

    def create_user(self, email, password, name, telep,documento,placa,tipoVehi,movilidad):

        if not email and not password and not name and not telep:
            return ValueError('Datos faltantes o inválido para el registro')

        makeUser = self.model(email = email, name=name, telephone=telep, placa_vehiculo= placa, type_vehiculo=tipoVehi, id = documento, presentar_movilidad = movilidad)
        makeUser.set_password(password)
        makeUser.save(using=self._db)

        return makeUser

    def create_superuser(self, email, fullName, password, telep):
        superUser = self.create_user(email, password, fullName, telep)
        superUser.is_superuser = True
        superUser.is_staff = True
        superUser.save(using=self._db)
        return superUser


class modelUser(AbstractBaseUser, PermissionsMixin):
    id = models.IntegerField('Documento_User',primary_key=True)
    name = models.CharField('Nombre_User', max_length=100)
    email = models.EmailField('Email_User', max_length=80, unique=True)
    telephone = models.IntegerField('Telefono_User')
    placa_vehiculo = models.CharField('PlacaVehiculo', max_length=20)
    type_vehiculo = models.CharField('Tipo_Vehiculo', max_length=250)
    presentar_movilidad = models.BooleanField('Movilidad')
    password = models.CharField('Password', max_length=256)

    def save(self, **kwargs):
        self.password = make_password(self.password, 
        'mMUj0DrIK6vgtdIYepkIxN')
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['__all__']
    
