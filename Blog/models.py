from distutils.command.upload import upload
from tabnanny import verbose
from tkinter.tix import MAX
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=10000)
    contenido = models.CharField(max_length=10000)
    imagen = models.ImageField(upload_to = "blog", null = True, blank = True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'

    def __str__(self):
        return self.titulo
