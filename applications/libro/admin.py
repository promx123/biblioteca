from django.contrib import admin
from .models import Categoria, Libro 
# Register your models here.
admin.site.register(Libro)
admin.site.register(Categoria)