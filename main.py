import string
import random

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ""
    for i in range(longitud):
        contrasena += random.choice(caracteres) #escoge un carácter al azar de la variable caracteres (que tiene todos los simbolos que hay)
    return contrasena
        
longitud = int(input("¿Cual es la longitud de la contraseña deseada?"))

nueva_contrasena = generar_contrasena(longitud)
print("La nueva contraseña es:", nueva_contrasena)