import datetime
from itertools import count #esto es importante xq pone bien los formatos de las fechas
from django.db import models
from django.db.models import  Q , Count# esto sirve para consultas or
from django.contrib.postgres.search import TrigramSimilarity


class LibroManager(models.Manager):
    #managers para el modelo autor
    def listar_libros(self, kword):
        resultado = self.filter(
            titulo__icontains =kword,
            #fecha__range=('2000-01-01', '2022-01-01')
            )
        return resultado
    
    def listar_libros_trg(self, kword):
        
        if kword:
            resultado = self.filter(
            titulo__trigram_similar =kword,
            )
            return resultado
        else:
            return self.all()[:10]
            
        
    
    def listar_libros2(self, kword , fecha1 , fecha2):
        date1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()

        
        resultado = self.filter(
            titulo__icontains =kword,
            fecha__range=(date1 ,date2)
            )
        return resultado
    
    def listar_libros_categoria(self, categoria):
        
        return self.filter(
            categoria__id = categoria
        ).order_by('titulo')
        
    def add_autor_libro(self, libro_id, autor ):
        libro = self.get(id = libro_id)
        libro.autores.add(autor) #si queres eliminar es lo mismo pero en vez de add es remove
        return libro
    
    def libros_num_prestamos(self):
        resultado = self.aggregate(# agregate devuelve un diccionario y este es para encontrar un valor tipo operacion aritmetica como promedio
            num_prestamos=Count('libro_prestamo')
        )
        return resultado
        
        
class CategoriaManager(models.Manager):
    
    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id = autor
        ).distinct() #es para que no se repitan consultas
        
    def listar_categoria_libros(self):
        resultado = self.annotate( #anotatte devueve un queryset y este es el mejor para devolver un conteo
            num_libros =Count('categoria_libro')#esto es para contar la cantidad de libros que tiene una categoria
        )
        """ todo esto de aca abajo es para probar en la shell si anda bien la consulta de arriba
        for r in    resultado:
            print('*******')
            print('r, r.num_libros')
        """
        return resultado
    
    def num_libros_prestados(self):
        resultado = self.annotate(
            num_prestado = Count('libro_prestamo')
        )
        
        return resultado