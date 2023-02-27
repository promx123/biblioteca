from PIL import Image

def optimize_image(sender , instance,  **kwargs): #sender = para donde va la funcion
    #print("===================")
    #print(instance)
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality = 20, optimize = True)
    