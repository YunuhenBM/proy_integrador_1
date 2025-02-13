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
print(f"Comienzas con {vidas} vidas 💚💚💚💚💚") 

# Actualizar el ahorcado
# ¿Está la letra en la palabra?
#Para verificar si la letra está en la palabra, debemos recorrer la palabra. Para ello, será
#Necesario un for in range
#Aquí iría otro while
while "_" in palabra_oc and vidas > 0:
    letra = input("Ingrese una letra: ").lower().strip()
    #Validación de entrada
    while not (len(letra) == 1 and letra.isalpha()):
        letra = input("Su entrada es inválida. Ingrese una letra: ").lower().strip()

    if letra in palabra_sec:
        for i in range(len(palabra_sec)):
            if palabra_sec[i] == letra:
                palabra_oc[i] = letra
        print("😍 Correcto, acertaste la letra")
        print(f"Tienes {vidas} vidas")
    else:
        print("La letra no se encuentra en la palabra. Vuelve a intentarlo")
        vidas -= 1
    print("".join(palabra_oc))
    print(f"Te quedan {vidas} vidas")

#Fin del juego
if "_" not in palabra_oc:
    print("Ganaste el juego. ¡Felicidades! 🙌")
else: 
    print("Perdiste 😪 )")



