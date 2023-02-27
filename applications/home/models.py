from pyexpat import model
from django.db import models

# Create your models here.

class Persona(models.Model):
    full_name = models.CharField('nombres', max_length=50)
    pais = models.CharField('Pais', max_length=30)
    pasaporte = models.CharField( 'Pasaporte', max_length=50)
    edad = models.IntegerField()
    apelativo = models.CharField( 'Apelativo', max_length=50)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table= 'Persona'  #con esto pones como queres que se llame este modelo en la base de datos
        unique_together = ['pais' , 'apelativo'] #no se va a repetir estos 2 en la base de datos
        constraints = [ #es un restriccion
            models.CheckConstraint(check=models.Q(edad__gte=18) , name= 'edad_mayor_18')
        ]
        abstract = True # con esto haces que no se cree estas tablas en base de datos pero se puede usar como herencia

    def __str__(self):
        return self.full_name

#herencia de clase persona en el modelo
class Empleados(Persona):
    empleo = models.CharField('Empleo', max_length=50) 
    
class Cliente(Persona):
    email = models.EmailField( 'Email', max_length=254)
   
