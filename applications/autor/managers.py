from django.db import models
from django.db.models import  Q # esto sirve para consultas or
class AutorManager(models.Manager):
    #managers para el modelo autor
    def buscar_autor(self, kword):
        resultado = self.filter(
            nombre__icontains =kword
            )
        return resultado
    
    def buscar_autor2(self, kword):
        resultado = self.filter(
            Q(nombre__icontains =kword) | Q(apellidos__icontains =kword)
            )
        return resultado
    
    def buscar_autor3(self, kword):
        resultado = self.filter(
            nombre__icontains =kword
            ).exclude(Q(edad__icontains = 45) | Q(edad__icontains =21))
        return resultado
    
    def buscar_autor4(self, kword):
        resultado = self.filter(
            edad__gt = 20 ,  #__gt es mayor que y una , es para indicar un and 
            edad__lt = 45 #__lt es menor que  
            ).order_by('apellidos' , 'id')
        return resultado
    
    