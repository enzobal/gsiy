# box/models.py fotos subidas por el admin

from django.db import models

class Foto(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='fotos/')
    descripcion = models.TextField(blank=True, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


# box/models.py videos subidos por el admin
class Video(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    video = models.FileField(upload_to='videos/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
# para rutina personalizada
from django.db import models
from django.contrib.auth.models import User, Group

class SpecialRoutine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    visible_to_groups = models.ManyToManyField(Group, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# fin rutina 