#Proyecto Integrador

## Hacer la palabra
import random 
palabras = ["programacion", "escuela", "computadora", "github", "python", "java", "codigo", "estudiar"]
palabra_sec = random.choice(palabras)
l = len(palabra_sec)
palabra_oc = ["_"]* l
palabra_unida = "".join(palabra_oc)

##Comienza el juego
print("Comienza el juego 👀")
print(palabra_unida)
print(f"La palabra oculta tiene {l} letras") 
letra = input("Ingrese una letra: ").lower().strip()

#Validación de entrada
while not (len(letra) == 1 and letra.isalpha()):
    letra = input("Su entrada es inválida. Ingrese una letra: ")

