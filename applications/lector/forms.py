from dataclasses import fields
from django import  forms

from applications.libro.models import Libro

from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    
    class  Meta:
        model = Prestamo
        fields = (
            'lector',
            'libro',
        )
        
class MultiplePrestamoForm(forms.ModelForm):
    #asi se hace xq no hay many to many 
    libros = forms.ModelMultipleChoiceField(
        queryset= None,
        required = True,
        #los widgets son como herramientas
        widget = forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Prestamo
        fields = (
            'lector',
            
        )
        
    #este es para que se muestre de entrada un valor en html
    def __init__(self, *args, **kwargs):
        super(MultiplePrestamoForm, self).__init__(*args, **kwargs)
        #aca podes crear lo que se te cante
        self.fields['libros'].queryset = Libro.objects.all()
    