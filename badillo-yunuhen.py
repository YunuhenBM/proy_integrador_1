#Proyecto Integrador

## Hacer la palabra
import random 
palabras = ["programacion", "escuela", "computadora", "github", "python", "java", "codigo", "estudiar"]
palabra_sec = random.choice(palabras)
l = len(palabra_sec)
palabra_oc = ["_"]* l
palabra_unida = "".join(palabra_oc)
vidas = 5

##Comienza el juego
print("Comienza el juego 👀🦑")
print(palabra_unida)
print(f"La palabra oculta tiene {l} letras")
print(f"Comientas con {vidas} vidas 💚💚💚💚💚") 
letra = input("Ingrese una letra: ").lower().strip()

#Validación de entrada
while not (len(letra) == 1 and letra.isalpha()):
    letra = input("Su entrada es inválida. Ingrese una letra: ").lower().strip()

# Actualizar el ahorcado
# ¿Está la letra en la palabra?
#Para verificar si la letra está en la palabra, debemos recorrer la palabra. Para ello, será
#Necesario un for in range
#Aquí iría otro while

for i in range(len(palabra_sec)):
    if palabra_sec[i] == letra:
        palabra_sec[i] = letra
        print("😍 Correcto, acertaste")
        print(f"Tienes {vidas} vidas")
    else:
        print("La letra no se encuentra en la palabra. Vuelve a intentarlo")
        vidas -= 1
print("".join(palabra_oc))


