from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria_Prod (models.Model):
    nombre = models.CharField (max_length=50)
    created = models.DateTimeField (auto_now_add=True)
    updated = models.DateTimeField (auto_now_add=True)

    class Meta:
        verbose_name = "categoria_prod"
        verbose_name_plural =  "categorias_prod"

    def __str__(self):
        return self.nombre 

class Producto (models.Model):
    nombre = models.CharField (max_length=50)
    precio = models.FloatField ()
    disponibilidad = models.BooleanField(default=True)
    categorias = models.ForeignKey (Categoria_Prod, on_delete= models.CASCADE)
    created = models.DateTimeField (auto_now_add=True)
    updated = models.DateTimeField (auto_now_add=True)

    class Meta:
        verbose_name = "producto"
        verbose_name_plural =  "productos"

    def __str__(self):
        return self.nombre 