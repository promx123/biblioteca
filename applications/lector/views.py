from datetime import  date

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import  FormView

from .models import Lector, Prestamo
from .forms import PrestamoForm , MultiplePrestamoForm
#este puede ser que se borre
class RegistrarPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.' #se recarga la misma pagina
    
    def form_valid(self, form):
        prestamo = Prestamo(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            fecha_prestamo = date.today(),
            devuelto = False
            )
        prestamo.save()
        #funcion para reducir stock del libro
        
        libro = form.cleaned_data['libro']
        libro.stock = libro.stock - 1
        libro.save()
        
        
        return super(RegistrarPrestamo , self).form_valid(form)
    
    #####
    
class AddPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.' #se recarga la misma pagina
    
    def form_valid(self, form):
       #con esto validamos si el objeto esta y se creo
       obj , created = Prestamo.objects.get_or_create(
           lector = form.cleaned_data['lector'],
           libro = form.cleaned_data['libro'],
           devuelto = False,
           defaults = {#esto es para los demas campos que faltan
               'fecha_prestamo' : date.today()
           }
       )
       if created:
           return super(AddPrestamo , self).form_valid(form)
       else:
           return HttpResponseRedirect('/') #podes usar esta func para llamar un url con el name de los mismos.
        
        
####

class AddMultiplePrestamo(FormView):
    template_name = 'lector/add_multiple_prestamo.html'
    form_class = MultiplePrestamoForm
    success_url = '.' #se recarga la misma pagina
    
    def form_valid(self, form):
        #
       # print(form.cleaned_data['lector'])
       # print(form.cleaned_data['libros'])
        #
        prestamos = []
        for l  in  form.cleaned_data['libros']: #iteramos en esta queryset
             prestamo = Prestamo(
            lector = form.cleaned_data['lector'],
            libro = l,
            fecha_prestamo = date.today(),
            devuelto = False
            )
             prestamos.append(prestamo)  
        print (prestamos)
        Prestamo.objects.bulk_create(#esto registra todo en una consulta muy usado para los for
            prestamos
        )
        return super( AddMultiplePrestamo, self).form_valid(form)

