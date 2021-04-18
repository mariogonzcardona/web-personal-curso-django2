from django.db import models
from django.db.models import fields

# Create your models here.
class Project (models.Model):
    title=models.CharField(max_length=250,verbose_name="Titulo")
    description=models.TextField(verbose_name="Descripcion")
    image=models.ImageField(verbose_name="Imagen",upload_to="projects")
    link=models.URLField( null=True,blank=True,verbose_name="Enlace")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creacion")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de Actualizacion")
    
    #Metadata
    class Meta :
        verbose_name="proyecto"
        verbose_name_plural="proyectos"
        ordering = ['-created']

    # #Methods
    # def get_absolute_url(self):
    #     return reverse('url', args=[args])

    def __str__(self):
        return self.title