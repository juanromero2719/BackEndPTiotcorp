from django.db import models
from personas.models import Persona

# Create your models here.
class Tarea(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='tareas')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_limite = models.DateField()
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso'), ('Completada', 'Completada')], default='Pendiente')
    prioridad = models.IntegerField(choices=[(1, 'Baja'), (2, 'Media'), (3, 'Alta'), (4, 'Muy Alta'), (5, 'Crítica')], default=3)
    creada_en = models.DateTimeField(auto_now_add=True)
    actualizada_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo