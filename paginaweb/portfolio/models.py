
from django.db import models

# Create your models here.
class Project (models.Model):
    
    #Tabla de gestion automatica de atributos en la base de datos
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField( verbose_name="Descripción")
    image = models.ImageField(  verbose_name="Imagen", upload_to = "projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    update = models.DateTimeField(auto_now=True,  verbose_name="Fecha de Edición")
    

    class Meta:
        verbose_name ='sitio'
        verbose_name_plural ='sitios'
        ordering = ["-created"]
    def __str__(self):
        return self.title    