from django.db import models

# Create your models here.

class Cancion(models.Model):
    cancion_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200,default='',verbose_name='TITULO')
    url = models.CharField(max_length=200,default='',verbose_name='LINK')
    fecha_registro= models.DateTimeField(auto_now_add=True,verbose_name='FECHA DE REGISTRO')
    
    def __str__(self):
        return self.titulo