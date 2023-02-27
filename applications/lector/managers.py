import  datetime
from unittest import result
from django.db import  models
from django.db.models import Q, Count , Avg , Sum   #avg es para promedios
from django.db.models.functions import  Lower


class PrestamoManager(models.Manager):
    #prestamomanager
    
    def libros_promedio_edades(self):
        resultado = self.filter(
            libro__id='15'
        ).aggregate(
            promedio_edad = Avg('lector__edad'),
            suma_edad = Sum('lector_edad'),
        )
        return resultado
    
    
    def num_libros_prestados(self):
        resultado = self.values( # con values es la forma de usar el annotatebien
            'libro'
            ).annotate(
            num_prestado = Count('libro'),
            titulo =Lower('libro__titulo'), # __ es para acceder al contenido del foreign key
        )
        for r in resultado:
            print('=======')
            print (r , r['num_prestado']) #asi ingreso para un diccionario
        
        return resultado