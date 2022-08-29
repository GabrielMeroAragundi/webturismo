from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
options = {
        'guia': '¿Requiere guía turístico?',
        'lancha': '¿Incluir viaje en lancha',
        'hospedaje':'¿Incluir alojamiento?',
        'sendero':'¿Incluir sendero ecologico?',
        'salinas':'¿Incluir recorrido por salinas?',
        'museo':'¿Incluir recorrido por museo?',
        'carpas':'¿Incluir carpas para sol?'
    }

class Reserva(models.Model):

    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    cedula = models.CharField(max_length=10, verbose_name="Cédula")
    correo = models.CharField(max_length=70, verbose_name="Correo", null=True)
    telefono = models.CharField(max_length=13, verbose_name="Teléfono", null=True)
    
    adultos  = models.IntegerField(default=1,validators=[MinValueValidator(1)],verbose_name="Adultos")
    menores  = models.IntegerField(default=0,validators=[MinValueValidator(0)],verbose_name="Menores")

    fechaInicio = models.DateField(verbose_name="Fecha Inicio", null=True)
    fechaFin = models.DateField(verbose_name="Fecha Fin", null=True)

    guia = models.BooleanField(default=False, verbose_name="Incluir Guía Turístico")
    lancha = models.BooleanField(default=False, verbose_name="Incluir Recorrido en Lancha")
    hospedaje = models.BooleanField(default=False, verbose_name="Incluir Hospedaje")
    sendero = models.BooleanField(default=False, verbose_name="Incluir Recorrido por el Sendero Ecologico")
    salinas = models.BooleanField(default=False, verbose_name="Incluir Recorrido por Pampas Salineras")
    museo = models.BooleanField(default=False, verbose_name="Incluir Recorrido por el Museo")
    carpas = models.BooleanField(default=False, verbose_name="Incluir Carpas para Sol")
    

    def __str__(self):
        return f' Cliente: {self.nombre} {self.apellido}'