# Generated by Django 3.2.9 on 2021-11-17 15:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='modelEstacion',
            fields=[
                ('parqueadero', models.CharField(max_length=250, primary_key=True, serialize=False, unique=True)),
                ('cupos_vehiculos', models.IntegerField()),
                ('cupos_motocicletas', models.IntegerField()),
                ('cupos_bicicletas', models.IntegerField()),
                ('cupos_esp_discapaci', models.IntegerField()),
                ('tarifa_vehiculos', models.IntegerField()),
                ('tarifa_motocicletas', models.IntegerField()),
                ('tarifa_bicicletas', models.IntegerField()),
                ('tarifa_esp_discapaci', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='modelReservas',
            fields=[
                ('id_Reserva', models.AutoField(primary_key=True, serialize=False)),
                ('locationParqueadero', models.CharField(max_length=250)),
                ('tipo_vehiculo', models.CharField(max_length=250)),
                ('fecha_hora_llegada', models.DateTimeField(default=django.utils.timezone.now)),
                ('tiempo_estimado', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='modelUser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Documento_User')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre_User')),
                ('email', models.EmailField(max_length=80, unique=True, verbose_name='Email_User')),
                ('telephone', models.IntegerField(verbose_name='Telefono_User')),
                ('placa_vehiculo', models.CharField(max_length=20, verbose_name='PlacaVehiculo')),
                ('type_vehiculo', models.CharField(max_length=250, verbose_name='Tipo_Vehiculo')),
                ('presentar_movilidad', models.BooleanField(verbose_name='Movilidad')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]