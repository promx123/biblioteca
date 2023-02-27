def update_libro_stock(sender , instance, **kwargs ):
    #actualizamos el stock si elimina un prestamo
    instance.libro.stock = instance.libro.stock + 1
    instance.libro.save()