from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# modelloo para imagen en el formulario
# models.py
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    localidad = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.user.username} Profile"
# fin modelo imagen

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    # Otros campos de la marca, si los necesitas

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    cantidad_disponible = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    # Otros campos según tus necesidades

    def __str__(self):
        return self.nombre



# formulario de contactos
class FormularioContacto(models.Model):
    tipo_consulta = [
        ('horarios', 'horarios'),
        ('profesores', 'profesores'),
        ('felicitarnos', 'felicitarnos'),
        ('critica constructiva', 'critica constructiva')
    ]
    disciplina = [
        ('crossfit', 'crossfit'),
        ('funcional kid', 'funcional kid'),
        ('jiu jitsu', 'jiu jitsu'),
        ('Otros', 'Otros')
    ]

    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    tipo_consulta = models.CharField(max_length=100, choices=tipo_consulta)
    profesor = models.CharField(max_length=100, choices=disciplina)
    mensaje = models.TextField()
    aviso = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

# fin formulario de contactos


class Discipline(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name



class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=20)  # e.g., 'Lunes', 'Martes', etc.
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.actividad.nombre} - {self.dia_semana} {self.hora_inicio} - {self.hora_fin}"

class UsuarioActividad(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.username} - {self.actividad.nombre} - {self.horario.dia_semana} {self.horario.hora_inicio}"

# models.py
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

class Cuota(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cuotas')
    fecha_inicio = models.DateField()
    fecha_vencimiento = models.DateField(blank=True, null=True)
    pagada = models.BooleanField(default=False)  # Campo para indicar si la cuota ha sido pagada

    def save(self, *args, **kwargs):
        if not self.fecha_vencimiento:
            self.fecha_vencimiento = self.fecha_inicio + timedelta(days=30)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Cuota de {self.usuario.username} - Vence el {self.fecha_vencimiento}"

#para el blog del home


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    video = models.FileField(upload_to='blog_videos/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    




