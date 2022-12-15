from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria= models.CharField(max_length = 60)
    def __str__(self):
        return self.categoria

class Noticia(models.Model):

    titulo = models.CharField(max_length= 150)
    cuerpo = models.TextField()
    imagen = models.ImageField(upload_to= 'noticias')
    categoria_noticia = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    fecha = models.DateField(auto_now=True)
    def __str__ (self):
        return self.titulo
