from django.db import models

# Create your models here.
class Servicio(models.Model):

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=100, decimal_places=2)
    duracion = models.CharField(max_length=2, help_text='En minutos')
    imagen = models.ImageField(upload_to='imagenes/', null=True )  # Imagen del servicio

    def __str__(self):
        return self.nombre