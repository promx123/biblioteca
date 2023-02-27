
from pickletools import optimize
from django.db import models
from django.db.models.signals import  post_save
#app de terceros
#signals
from .signals import optimize_image
#local apps
from applications.autor.models import Autor

from .managers import LibroManager , CategoriaManager
#signals
# Create your models here.
class Categoria(models.Model):
  nombre = models.CharField(max_length=30)
  
  objects = CategoriaManager() 
  
  def __str__(self):
      return str (self.id)  + '-' + self.nombre
  
class Libro(models.Model):
    categoria =models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='categoria_libro' #de esta forma accedo desde categoria al modelo libro                             
    )
    
    autores = models.ManyToManyField(Autor)
    titulo =  models.CharField(max_length=50)
    fecha =  models.DateField('Fecha de lanzamiento')
    portada =  models.ImageField(upload_to='portada' , blank=True)
    visitas = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default = 0)
    
    objects = LibroManager()
    
    class Meta:
        verbose_name = 'Libro'        
        verbose_name_plural = 'Libros'
        ordering = ['titulo', 'fecha' ]
    
    def __str__(self):
        return  str (self.id) + '-' + self.titulo 
    

    
post_save.connect(optimize_image, sender = Libro ) #despues del guardado ejecuta un funcion y la manda un modelo.