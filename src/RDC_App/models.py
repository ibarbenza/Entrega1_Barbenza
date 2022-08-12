from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Vinos(models.Model):

    bodega = models.CharField(max_length=150)
    etiqueta = models.CharField(max_length=150)
    cosecha = models.CharField(max_length=4, blank=True, null=True)
    cc_botella = models.IntegerField(default=750)
    precio_botella = models.FloatField()
    precio_caja = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.bodega} - {self.etiqueta}"

class Bebidas(models.Model):
    clase = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    etiqueta = models.CharField(max_length=150)
    cc_botella = models.IntegerField(default=750)
    precio_botella = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.clase} - {self.marca} {self.etiqueta}"    

class Copas(models.Model):
    nombre = models.CharField(max_length=150)
    precio = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"

class Reseña(models.Model):
    titulo = models.CharField(max_length=50)
    fecha = models.DateField(default=datetime.now)
    contenido = models.CharField(max_length=2000)
    rating = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.titulo